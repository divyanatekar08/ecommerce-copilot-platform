# Real-Time Intelligent E-Commerce Platform

An enterprise-grade, asynchronous e-commerce platform built with FastAPI, PostgreSQL, LangGraph, Qdrant Vector Search, Celery, and Stripe.

---

## 🏗️ Tech Stack

* **Backend**: FastAPI (Python 3.13)
* **Database**: PostgreSQL (SQLAlchemy 2.0 Async + `asyncpg`)
* **Vector DB**: Qdrant (`qdrant-client` + `fastembed`)
* **AI Orchestration**: LangGraph / LangChain
* **Task Queue**: Celery + Redis
* **Payments**: Stripe API (`PaymentIntent` + Webhook verification)
* **Validation & Security**: Pydantic v2, `email-validator`, Passlib, JOSE JWT

---

## 📁 Directory Structure

```text
ecommerce-copilot-platform/
├── backend/
│   ├── app/
│   │   ├── api/          # Route handlers (payments, products, AI endpoints)
│   │   ├── core/         # Config, database setup, security settings
│   │   ├── models/       # SQLAlchemy 2.0 ORM models
│   │   ├── schemas/      # Pydantic v2 validation schemas
│   │   └── main.py       # FastAPI application entrypoint
│   └── requirements.txt  # Python dependencies
├── .gitignore
└── README.md