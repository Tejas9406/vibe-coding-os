---
name: system-design-engine
description: Expert distributed system architecture and engineering decision engine. Use when the user requests system design, architecture blueprints, distributed patterns, high concurrency scalability, microservices vs monolith decisions, CAP/BASE trade-offs, caching strategies (Redis, Cache-Aside), message queue selection (Kafka, RabbitMQ), database sharding, or observability.
tags: ["system-design", "architecture", "distributed-systems", "microservices", "scalability", "caching", "message-queues"]
version: 2.0.0
---

# 🏛️ System Design & Architecture Decision Engine

> **Expert-level distributed system architecture and decision support guide, covering the complete lifecycle from requirements analysis to component selection and failure modes.**

---

## 1. System Type Routing

Selecting the appropriate system archetype based on business requirements is the starting point of system design.

### Six Core System Archetypes

| System Type | Core Characteristic | Typical Scenarios | Key Technical Challenges |
| :--- | :--- | :--- | :--- |
| **High Concurrency** | QPS > 100,000 / sec | Flash sales, ticketing, viral social events | Traffic throttling, connection pooling, hotspot caches |
| **High Availability** | SLA > 99.99% | Financial payments, telecom core, auth | Multi-region disaster recovery, failover, auto-healing |
| **Data Intensive** | PB-scale storage, trillion rows | Big data analytics, search engines, logs | Sharding, cold/hot data tiering, query indexing |
| **Compute Intensive** | CPU/GPU heavy, long execution | AI inference, scientific computing, rendering | Batch processing, GPU scheduling, distributed compute |
| **Real-Time** | Sub-100ms latency | IoT streams, multiplayer gaming, chat | Event-driven, stream processing (Flink), low-latency nets |
| **Offline / Batch** | Batch jobs, T+1 schedule | Data warehousing, reporting, backups | Job orchestration, resource elasticity, DAG dependencies |

### Routing Decision Tree

```
Input Requirements Analysis
    │
    ▼
QPS > 100,000? ──YES──▶ Prioritize High Concurrency Architecture
    │ NO
    ▼
SLA > 99.99%? ──YES──▶ Prioritize High Availability (Multi-active / CP/AP)
    │ NO
    ▼
Storage > 10 TB? ──YES──▶ Prioritize Data Intensive (Sharding / Data Lake)
    │ NO
    ▼
Latency < 100ms? ──YES──▶ Prioritize Real-Time Systems (Event-Driven / Cache)
    │ NO
    ▼
Compute Load > 80% CPU/GPU? ──YES──▶ Prioritize Compute Intensive (Async Workers)
    │ NO
    ▼
Offline Analytics / Reporting ──▶ Prioritize Batch Pipelines (ETL / OLAP)
```

---

## 2. Architecture Style Decision

### Architecture Style Comparison

| Style | Best For | Advantages | Disadvantages | Team Prerequisite |
| :--- | :--- | :--- | :--- | :--- |
| **Monolith** | Startups, MVPs, small tools | Simple, fast deploy, easy debugging | Hard to scale independently, coupled | Low |
| **Modular Monolith** | Growing teams, structured domain | Clear boundaries without network latency | Requires strict architectural discipline | Medium |
| **Microservices** | Large systems, multi-team domains | Independent deploy, diverse tech stacks | Network overhead, distributed tracing, ops complexity | High |
| **Event-Driven** | Async workflows, loose coupling | Highly scalable, resilient to outages | Eventual consistency, debugging complexity | Medium-High |
| **Serverless** | Intermittent load, webhooks, edge | Pay-per-use, zero server maintenance | Cold starts, vendor lock-in, state limits | Medium |
| **CQRS** | Read/write asymmetry, complex queries | Optimized reads/writes independently | Code duplication, sync lag complexity | High |

### Evolutionary Architecture Path

```
Phase 1: Simple Monolith (MVP)
    │ Pain: Code bloat, deploy conflicts
    ▼
Phase 2: Modular Monolith (Growth)
    │ Pain: Database bottleneck
    ▼
Phase 3: App Cluster + Read/Write DB Replicas (Scaling)
    │ Pain: Single database write ceiling
    ▼
Phase 4: Domain Splitting + Caching Layer (Scale-out)
    │ Pain: Service coordination overhead
    ▼
Phase 5: Microservices / Event Mesh + Containers (Enterprise)
```

---

## 3. Distributed System Principles

### CAP Theorem Application

```
               Consistency
                   /\
                  /  \
                 /    \
                /  P   \
               /   ↖    \
              /    C    \
             ──────────────
      Partition Tolerance ── Availability
```

- **CA**: Monolithic RDBMS (PostgreSQL/MySQL single primary). *Impossible across network partitions.*
- **CP**: Strong consistency under partitions (etcd, ZooKeeper, Consul, CockroachDB). Prefers rejecting requests over serving stale data.
- **AP**: Maximum availability under partitions (Cassandra, DynamoDB, CouchDB). Returns potentially stale data rather than failing.

### BASE Theory
- **Basically Available**: Guarantee core features remain functional during failures via graceful degradation.
- **Soft State**: Accept that data may be in transition or temporarily inconsistent across replicas.
- **Eventually Consistent**: Ensure all replicas converge to identical states given sufficient time.

---

## 4. Caching Strategy & Failure Modes

### Core Caching Patterns

1. **Cache-Aside (Standard Pattern)**
   - **Read**: Check cache → On Hit, return. On Miss, read DB → Write to cache → Return.
   - **Write**: Write to DB first → Invalidate/delete cache key (do NOT update cache directly to avoid race conditions).

2. **Read/Write-Through**: The application interacts solely with the cache layer; the cache provider reads and writes synchronously to the backing database.

3. **Write-Behind (Write-Back)**: Writes are acknowledged in cache immediately and queued for asynchronous batch writes to DB. High throughput, but risks data loss on node failure.

### Cache Failure Modes & Defense

| Failure Mode | Root Cause | Symptoms | Remediation Strategy |
| :--- | :--- | :--- | :--- |
| **Cache Penetration** | Querying keys that don't exist in DB | Traffic bypasses cache and hammers DB | 1. Bloom Filters<br>2. Cache null values with short TTL (30s)<br>3. Input format validation |
| **Cache Breakdown** | Hotspot key expires while under massive concurrency | Massive simultaneous DB queries for the same key | 1. Mutex lock (`SETNX`) on cache refill<br>2. Logical expiration (background refresh)<br>3. Zero-expiry for evergreen hotkeys |
| **Cache Avalanche** | Large batch of keys expire at the exact same second | DB CPU spikes to 100% and crashes | 1. Add random jitter to TTL (`TTL = base + rand(1-60)s`)<br>2. Multi-tier cache (L1 in-memory + L2 Redis)<br>3. Circuit breakers & rate limiting |

---

## 5. Message Queue Selection

| Dimension | Apache Kafka | RabbitMQ | Apache Pulsar | Redis Stream |
| :--- | :--- | :--- | :--- | :--- |
| **Throughput** | 1,000,000+ msg/sec | ~50,000 msg/sec | 1,000,000+ msg/sec | ~50,000 msg/sec |
| **Latency** | Milliseconds | Microseconds | Milliseconds | Sub-millisecond |
| **Ordering** | Per partition | Per queue | Per partition | Per stream |
| **Replay / Retention** | Log-based (re-read from offset) | Queue-based (consumed = deleted) | Tiered storage (S3 offload) | Memory limited |
| **Best Scenario** | Event streaming, log pipelines, telemetry | Complex routing, RPC, financial transactions | Multi-tenant cloud-native messaging | Simple lightweight async tasks |

---

## 6. Observability Pillars (OpenTelemetry Standard)

1. **Structured Logs**:
   - Always output JSON formatted logs.
   - Standard keys: `timestamp`, `level`, `trace_id`, `span_id`, `service`, `user_id`, `duration_ms`.
   - Never log unmasked PII, credentials, or full payload dumps.

2. **Metrics (RED & USE Methods)**:
   - **RED Method** (for request-driven services): **R**ate (QPS), **E**rrors (5xx rate), **D**uration (P50/P95/P99 latency).
   - **USE Method** (for resources): **U**tilization (% busy), **S**aturation (queue length), **E**rrors.

3. **Distributed Tracing**:
   - Propagate W3C `traceparent` headers across all service and HTTP/gRPC boundaries.
   - Trace critical database queries, external API calls, and message pub/sub.

---

## 7. 10 Anti-Patterns to Avoid

1. **Premature Microservices**: Splitting into 10 services before understanding domain boundaries. *Fix: Start with a Modular Monolith.*
2. **Database as a Message Queue**: Polling SQL tables (`status = 'PENDING'`) at high frequency. *Fix: Use Redis Stream or RabbitMQ.*
3. **Missing Idempotency**: Payment or order endpoints failing to check `Idempotency-Key`. *Fix: Use distributed locks + unique database constraints.*
4. **Cascading Synchronous Calls**: Service A calls B calls C calls D synchronously. *Fix: Introduce async event messaging or BFF (Backend for Frontend).*
5. **No Timeout / Circuit Breaker**: Downstream service slowdown freezes entire upstream connection pool. *Fix: Enforce aggressive HTTP client timeouts and circuit breakers (e.g. Resilience4j).*
6. **Hardcoded Configuration**: Storing secrets or URLs in code. *Fix: 12-Factor App config via environment variables.*
7. **Single Point of Failure (SPOF)**: A single non-replicated Redis, DB, or load balancer. *Fix: Active-passive failover or clustered deployments.*
8. **Unindexed High-Traffic Queries**: Filtering or sorting by columns without composite indexes. *Fix: Analyze execution plans (`EXPLAIN ANALYZE`).*
9. **Ignoring Backpressure**: Producers overwhelming consumer workers without flow control. *Fix: Rate limiting, worker pooling, and dead-letter queues.*
10. **All-or-Nothing Deployments**: Deploying big-bang updates directly to 100% of production users. *Fix: Canary releases or Blue/Green deployments.*

---

## 8. System Design Review Checklist

- [ ] **Capacity & Scale**: Have you estimated peak QPS, daily read/write volume, and storage growth for 12 months?
- [ ] **Single Point of Failure**: Is every layer (DNS, LB, App, Cache, DB, Queue) redundant?
- [ ] **Data Consistency**: Are write conflicts handled (optimistic locking / transactions / distributed locks)?
- [ ] **Failure Blast Radius**: If the primary database or external payment gateway goes down, does the app degrade gracefully?
- [ ] **Security Baseline**: Are all endpoints authenticated, rate-limited, and TLS-encrypted?
