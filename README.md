<div align="center">

# 🛒 Real-Time Intelligent E-Commerce Copilot

**An Enterprise-Grade, Asynchronous E-Commerce Engine Powered by FastAPI & LangGraph Agentic Search**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python_3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Qdrant](https://img.shields.io/badge/Qdrant_Vector_DB-DC2626?style=for-the-badge&logo=qdrant&logoColor=white)](https://qdrant.tech/)
[![Stripe](https://img.shields.io/badge/Stripe_Payments-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://stripe.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

</div>

## 📌 Executive Summary

**E-Commerce Copilot Platform** is an ultra-fast, event-driven backend platform designed for next-generation online retail. It bridges modern transactional e-commerce workflows (inventory management, order fulfillment, Stripe checkout verification) with intelligent AI shopping copilot agents built using **LangGraph**, **Gemini API**, and **Qdrant Vector Search**.

---

## 🔥 Key Features

* **⚡ Fully Asynchronous Core**: High-throughput FastAPI backend powered by SQLAlchemy 2.0 Async ORM and `asyncpg`.
* **💳 Event-Driven Stripe Integration**: Secure `PaymentIntent` processing paired with automated webhook verification handlers.
* **🧠 Agentic Shopping Copilot**: Context-aware product recommendations and conversation workflows orchestrated via **LangGraph** & **Google Gemini**.
* **🔍 Semantic Product Search**: Fast, dense vector embeddings provided by **Qdrant Vector DB** and `fastembed`.
* **📦 Asynchronous Task Pipeline**: Celery and Redis message broker handling distributed background jobs and notifications.

---

## 🏛️ System Architecture

```text
               +----------------------------------+
               |        React Frontend / Web      |
               +----------------------------------+
                                |
                                v
               +----------------------------------+
               |      FastAPI Gateway Router     |
               +----------------------------------+
                 /              |              \
                /               |               \
               v                v                v
     +---------------+  +---------------+  +---------------+
     |  PostgreSQL   |  | Qdrant Vector |  | LangGraph AI  |
     | (Orders/DB)   |  | (Embeddings)  |  |  (Copilot)    |
     +---------------+  +---------------+  +---------------+
              \                 |                 /
               +----------------+----------------+
                                |
                                v
                      +-------------------+
                      |   Stripe API      |
                      +-------------------+
