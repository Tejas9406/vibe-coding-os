---
name: devops-decision-engine
description: Expert DevOps engineering, CI/CD pipeline automation, container orchestration (Docker, Kubernetes), GitOps, infrastructure as code (Terraform), and cloud deployment decision support. Use when setting up CI/CD workflows, choosing deployment infrastructure, configuring monitoring/alerting, or defining container strategies.
tags: ["devops", "ci-cd", "docker", "kubernetes", "gitops", "infrastructure", "terraform", "monitoring"]
version: 2.0.0
---

# 🚀 DevOps & CI/CD Decision Engine

> **Expert DevOps engineering guidelines, pipeline automation patterns, container orchestration, and deployment strategy selection.**

---

## 1. DevOps Maturity Routing

DevOps maturity levels determine the appropriate tooling, pipeline design, and implementation priorities.

### Maturity Matrix

| Level | Name | Characteristics | Automation | Deployment Frequency | Lead Time to Deploy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L0** | Manual | Manual shell deploys, undocumented, ad-hoc | 0–10% | Monthly / Quarterly | Days to weeks |
| **L1** | Basic Automation | Build scripts, basic CI, unit test runners | 20–40% | Bi-weekly / Weekly | Hours to 1 day |
| **L2** | Continuous Integration | Automated build & test on PR, linting, quality gates | 50–70% | Daily / Weekly | Minutes to hours |
| **L3** | Continuous Delivery | Automated non-prod deploys, feature flags, staging | 75–90% | Daily | Minutes |
| **L4** | Continuous Deployment | Full zero-touch deploy to production, canary / GitOps | 90–99% | Multiple per day | Minutes to seconds |

---

## 2. CI/CD Tool Selection Matrix

| Dimension | GitHub Actions | GitLab CI | Jenkins | ArgoCD | Tekton |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Learning Curve** | Low / Fast setup | Medium | High / Steep | Medium | Steep |
| **Integration** | Native GitHub ecosystem | Native GitLab ecosystem | Plugin-heavy, self-hosted | Native Kubernetes | Native Kubernetes |
| **Cost Model** | Free tier for public repos | Free tier / Self-hosted | Free software + infra cost | Open source | Open source |
| **Architecture** | Hosted / Self-hosted runners | Hosted / Self-hosted runners | Master-Agent cluster | Pull-based GitOps operator | Pipeline CRDs on K8s |
| **Best Scenario** | GitHub-hosted codebases | Integrated DevOps platforms | Legacy enterprise pipelines | Declarative K8s deployments | Cloud-native CI engines |

### Recommended Tool Stacks by Team Scale

- **Startup / Solo Hacker**: GitHub Actions + Vercel / Railway / Fly.io + Supabase (Zero ops overhead)
- **Mid-Sized Team**: GitHub Actions / GitLab CI + Docker + AWS ECS / GCP Cloud Run + Datadog / Grafana Cloud
- **Cloud-Native / Enterprise**: GitHub Actions + ArgoCD + EKS/GKE Kubernetes + Terraform + Prometheus/Grafana

---

## 3. Container Orchestration Selection

| Criteria | Docker Compose | Docker Swarm | HashiCorp Nomad | Managed Kubernetes (EKS/GKE) |
| :--- | :--- | :--- | :--- | :--- |
| **Complexity** | Extremely Low | Low | Medium | High |
| **Setup Time** | 5 minutes | 1 hour | Half day | Days / Weeks |
| **Resource Overhead**| Minimal | Minimal | Low | Medium to High |
| **Workload Types** | Single-host containers | Multi-host containers | Containers, Binaries, VMs | Containers only |
| **Best For** | Local dev & small VPS | Lightweight multi-node | Hybrid multi-workload | Microservices, autoscaling clusters |

---

## 4. GitOps Workflow & Branching Strategy

### Branching Strategies

1. **Trunk-Based Development (Recommended for Modern Teams)**:
   - Developers work in short-lived feature branches (< 1 day).
   - Merged directly into `main` after automated CI passes.
   - Requires feature flags (LaunchDarkly, Unleash, PostHog) to hide incomplete features.
2. **GitHub Flow**:
   - Feature branches branch from `main`, open PRs, pass review and CI, deploy to staging/prod on merge.
3. **GitFlow (Legacy)**:
   - `develop`, `release`, `hotfix`, `master`. High overhead; use only when releasing discrete versioned artifacts (e.g. mobile apps, embedded software).

### Declarative GitOps Architecture

```
Developer Git Commit
        │
        ▼
GitHub Actions (CI)
  ├── 1. Run Linters & Tests
  ├── 2. Build & Scan Container Image
  └── 3. Push Image to Registry (ECR / GHCR)
        │
        ▼ Update Image Tag in Config Repo
GitOps Repository (Declarative K8s Manifests)
        │
        ▼ Pull-based reconciliation
ArgoCD / Flux Operator (Inside Kubernetes)
        │
        ▼ Sync State
Live Kubernetes Cluster
```

---

## 5. Security Gates (DevSecOps)

Integrate security checks directly into the CI pipeline:

1. **SAST (Static Application Security Testing)**:
   - Tooling: SonarQube, Semgrep, CodeQL.
   - Purpose: Scans source code for SQL injections, XSS, insecure cryptography before build.
2. **SCA (Software Composition Analysis)**:
   - Tooling: Snyk, Dependabot, Trivy.
   - Purpose: Identifies known vulnerabilities (CVEs) in third-party dependencies (`npm`, `pip`, `cargo`).
3. **Secret Scanning**:
   - Tooling: Gitleaks, TruffleHog.
   - Purpose: Blocks commits containing API keys, private keys, or passwords.
4. **Container Image Scanning**:
   - Tooling: Trivy, Clair, AWS ECR Inspector.
   - Purpose: Scans base OS images and libraries for vulnerabilities before deployment.

---

## 6. Three-Tier Quality Gate Checklist

### P0 — Merge & Deploy Blocker (Must Pass 100%)
- [ ] Build and compilation succeeds with 0 errors.
- [ ] Automated test suite passes 100%.
- [ ] Secret scanner passes with 0 leaked credentials.
- [ ] Container image build succeeds and contains no Critical CVEs.
- [ ] Database migration scripts validated against staging replica.

### P1 — Strongly Recommended Gates
- [ ] Test coverage exceeds team minimum (e.g., 80% line coverage on new code).
- [ ] Linter and formatter (Prettier, Black, ESLint, Ruff) report 0 errors.
- [ ] Dependency vulnerabilities evaluated (no High/Critical CVEs without approved waiver).
- [ ] Docker image sizes optimized (multi-stage builds, Alpine/Distroless bases).

### P2 — Continuous Improvement
- [ ] Automated canary release or preview environment generated.
- [ ] Cloud cost impact estimated (Infracost for Terraform).
- [ ] API documentation (OpenAPI / Swagger) auto-updated and verified.