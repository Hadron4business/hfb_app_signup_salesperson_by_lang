# Signup Salesperson by Language

Assigns a salesperson to a new website customer based on the language of the page they signed up on.

## What it does

- **By language** - Each language can have its own Registration Salesperson.
- **Automatic** - The contact gets the salesperson at the moment of signup. No manual work.
- **Safe fallback** - A language without a salesperson uses the Salesperson of the website.
- **Staff stay in control** - It runs once. A salesperson you change later is never overwritten.
- **Standard fields** - Uses the normal Salesperson field of the contact, so CRM and sales work as before.
- **No code** - One field on each language.

## How to use it

1. Make sure the website has the languages you need: Website > Configuration > Settings > Languages.
2. Open Settings > Translations > Languages (developer mode may be needed to see the menu) and open a language.
3. Set the Registration Salesperson and save. Repeat for every language.
4. Optionally, with the eCommerce app installed, set a default Salesperson on the website (Website > Configuration > Settings, Shop section) as a fallback.
5. A visitor registers on a page in that language (for example /de/web/signup).
6. Open the new contact: Salesperson is already filled in.

## Good to know

- The language is the one of the page the visitor registered on, not their country or postal code.
- Contacts created in the back office, by import or through other flows are not touched.
- If neither the language nor the website has a salesperson, the contact is left as Odoo creates it.
- Customers who sign up through an invitation link (portal invitation) go through the same signup and are covered too.

## Technical

- `models/res_lang.py` - field `registration_salesperson_id` on `res.lang`.
- `controllers/main.py` - extends `AuthSignupHome.do_signup` and writes `user_id` on the new contact.
- Depends on: `auth_signup`, `website`.

## Status

Source: client module (Odoo 18); detached from a client-specific signup module and now extends the standard `AuthSignupHome`. Odoo 18 build.
