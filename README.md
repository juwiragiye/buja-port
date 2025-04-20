# buja-port

 Digitize and centralize Bujumbura’s public service delivery, starting with permits, tax services, and a job portal, while ensuring multi-access for citizens, NGOs, tourists, and contractors via web and offline (USSD).

## 🧑‍🤝‍🧑 Target Users

- Regular Citizens  
- Private Contractors  
- NGOs  
- Tourists  

### 👥 User Roles and Access Levels

- Citizen  
- Guest (Tourist)  
- Government Official  
- Admin  
- Contractor  
- NGO Representative  

---

## 📦 Core Modules (Initial MVP)

1. **Permits Service** – Building permits, event permits, etc.  
2. **Tax Services** – Filing, payment, history tracking  
3. **Job Portal** – Post jobs, apply for jobs, track applications  

---

## 💻 Frontend Stack

- **React.js** (TypeScript)  
- TailwindCSS for styling  
- Next.js (Optional SSR for performance)  
- PWA support for offline capabilities  
- i18n for multilingual support (Kirundi, French, English, Swahili)  

## 🛠 Backend Stack

- **FastAPI** (Python)  
- PostgreSQL (Relational DB)  
- Redis (for caching, session store)  
- Celery + RabbitMQ (Background tasks)  
- Stripe Integration (Payment APIs)  
- USSD integration (for offline/feature phone access)  
- REST API + OpenAPI docs  

---

## 📱 Mobile/Offline Support

- **USSD System** connected to API  
- Optional future: React Native or Flutter app  

---

## 🔐 Authentication & Security

- OAuth (Google, Facebook, Apple)  
- Mobile Number Login (OTP)  
- 2FA (TOTP or SMS-based)  
- Bank Login Integration  
- Role-based access control (RBAC)  

---

## ⚖️ Open Source License

- **Creative Commons Non-Commercial (CC BY-NC-SA 4.0)**  
  - Allows sharing and adapting  
  - Must attribute  
  - Non-commercial use only  

---

## 🧱 Deployment Architecture

- Dockerized microservices  
- Docker Compose for development  
- Kubernetes (K8s) for production (optional)  
- PostgreSQL hosted on managed cloud (e.g. Supabase, RDS)  
- Object storage (e.g. S3, MinIO)  

---

## 🔁 CI/CD Pipeline

- GitHub Actions or GitLab CI  
- Linting & Testing (pytest, flake8, Jest)  
- Build & Deploy steps for Frontend and Backend  
- Automatic database migrations via Alembic  
- Preview environment for every PR  

---

## 🔌 API Strategy

- Versioned REST APIs (v1, v2...)  
- API Gateway (rate-limiting, analytics)  
- Public OpenAPI docs  
- JWT-based authentication  

---

## ☁️ Hosting Recommendations

- Backend: Render, Railway, or DigitalOcean App Platform  
- Frontend: Vercel or Netlify  
- USSD: Africa's Talking or Twilio  

---

## 🗃 Database Strategy

- Normalized schemas  
- Multi-tenant data separation (where needed)  
- Backups and replication plan  

---

## 📊 Monitoring & Analytics

- Sentry (Error monitoring)  
- Prometheus + Grafana (Backend performance)  
- Google Analytics or Plausible (Frontend)  

---

## 📚 Documentation

- Docusaurus site hosted on GitHub Pages  
- Setup, Contribution, API Reference, Architecture diagrams  

---

## 🧭 Future Module Ideas

- Civil registry (birth, marriage, death)
- Real-time transport tracking
- Digital health records
- Utility billing (water, electricity)
- Housing and land registry
- School enrollment & grading system
- Complaint management & whistleblowing

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

You are free to:

- **Share** — copy and redistribute the material in any medium or format

- **Adapt** — remix, transform, and build upon the material

Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

- **NonCommercial** — You may not use the material for commercial purposes.

- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

**You can read the full license text here:** [Link to the full license text file (e.g., LICENSE)](./LICENSE)

---
