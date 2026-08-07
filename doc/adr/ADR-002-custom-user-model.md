# ADR-002: Custom User Model Strategy

**Status:** Accepted

**Date:** 2026-07-19

## Title

Use Django's `AbstractUser` as the Foundation for the Custom User Model

## Context

FutMxStore is expected to grow from a simple academic materials platform into a multi-role ecosystem supporting:

* Customers (Students)
* Course Representatives
* Lecturers
* Vendors
* Administrators

The authentication system must remain compatible with Django's ecosystem while allowing future customization such as email-based authentication, role management, account verification, and additional identity fields.

The project philosophy is:

> **Architect for the Future. Implement for the Present.**

## Decision

Use Django's `AbstractUser` as the base class for the custom `User` model.

Configure Django to use the custom model from the beginning of the project by setting:

```python
AUTH_USER_MODEL = "authentication.User"
```

## Alternatives Considered

### Option 1: Django Default `User` + Profile

**Pros**

* Fast to start.
* Minimal initial configuration.
* Suitable for small projects with limited customization.

**Cons**

* Difficult to customize authentication later.
* Replacing the default user model after migrations is risky.
* Less flexibility for future identity requirements.

**Decision**

Rejected.

---

### Option 2: `AbstractBaseUser`

**Pros**

* Complete control over authentication.
* Maximum flexibility.
* Suitable for highly customized authentication systems.

**Cons**

* Requires implementing authentication logic, permissions, managers, and admin integration manually.
* Increases development time.
* Higher complexity for the MVP.

**Decision**

Rejected for Version 1.

---

### Option 3: `AbstractUser`

**Pros**

* Compatible with Django's authentication ecosystem.
* Supports future customization.
* Minimal additional configuration.
* Faster development.
* Easier onboarding for future contributors.

**Cons**

* Includes some fields that may eventually be customized or removed.

**Decision**

Accepted.

## Consequences

### Positive

* Supports future email-first authentication.
* Compatible with third-party Django packages.
* Reduces long-term technical debt.
* Simplifies future role expansion.
* Maintains rapid development for the MVP.

### Negative

* Some inherited fields may not be used immediately.
* Future customization may require overriding default behavior.

## Rationale

`AbstractUser` provides the best balance between flexibility and implementation speed.

It satisfies the current MVP requirements while allowing the authentication system to evolve without requiring a risky migration later.

This decision aligns with FutMxStore's engineering principle:

> **Architect for the Future. Implement for the Present.**
