# Architecture

Dextre is built on Python, using the Django web framework. Django works by having a set of "apps" that contain the backend and frontend of the site. These apps are each represented by a folder within the main directory.

Currently, within Dextre, we have the following apps:
- `accounts` - contains everything account management related. This includes queries with the SU API for creating member accounts, and managing shell accounts on the UWCS servers
- `api` - contains everything to do with OAuth authentication for other UWCS sites. The current list of these is:
  - UWCS Vote
  - Harmony
  - Amphi
  - Warwick.GG
- `blog` - is the main host of pages on the site and anything to do with the CMS (more on that later). The home page template is located here, along with templates for blog and about pages.
- `dextre` - the main app of the website. Contains settings for Django.
- `events` - anything to do with events on the website. Hooks into the CMS so event pages are managed within the CMS.
- `lib` - contains templates for reusable components across the website, like the sidebars and social media bubbles on the home page.
- `report` - a small app that powers the static report form on the website (`/report`) - this is purely a web form and does not store or communicate with the database in any way.

If new functionality being developed does not nicely fit within one of the above apps (for example, the report form functionality), create a new app for it and add the functionality in there.

There are also a few other folders of important note (although these are not apps):
- `.github` - contains YAML files for our CI and Dependabot configuration
- `media` - created during first setup, contains any images or documents uploaded to the CMS
- `static` - contains all the website's static files (CSS, JS, images)

Beyond the use of Python, there are a number of dependencies in use across the website:
- NPM is used to download all the CSS files from Bulma, the CSS framework in use on this site
- Sass (downloaded via NPM) is used to compress SCSS files into single CSS files for use in production
- Redis is used to power the cache for asynchronous tasks which are run using the Celery library
- Supervisor is used in production to run Celery for asynchronous tasks
- Cron is used in production to run the task that queries the SU API regularly to check for new members
- PostgreSQL is used for the website database

Currently, in production, Dextre is deployed using Apache2 and mod_wsgi. Sendgrid is used for sending emails, although this could later be moved to normal SMTP.

## SSO Integration
Functionality is provided within the website to allow users to authenticate with their Warwick ITS account instead of using the username and password provided by the site. On the frontend, this appears as a purple ("Warwick Aubergine") button that authenticates with Warwick's IDP service using Shibboleth.

Behind the scenes, a library called `django-saml-sp` is used. This provides us with the ability to do this authentication with little work from our side. Tne library creates metadata, which is provided to Warwick via a URL to both our live and staging sites. This authenticates us with Warwick and allows us to send and retrieve data required for authentication.

The attributes we currently receive from the University system are:
- First name
- Surname
- Student/Staff status
- Email address
- Department
- University ID

The university ID is mapped to Django's username field, as we use university IDs for account usernames. Student/staff status and department are not used currently (and are not stored anywhere in the backend), but could be used in the future if desired.

Any configuration from the UWCS site is managed in the Django administration panel. We currently have the ability to create accounts if one doesn't exist disabled, as accounts are only provided to those who have an active SU membership (or ex-exec), although the SU queries could be re-written to potentially enable this in the future.

If anything breaks, you should contact the IDG Helpdesk at the University for assistance.

_It is worth noting that since implementing this functionality originally, there are better libraries for this out there that work with Django, but changing it would require work from both us and IDG so there is little point in messing with something that works_

## The CMS
We use Wagtail for a CMS on the site - this provides functionality to create new about/blog/event pages on the fly, along with manage a couple of elements across the site (social media, footer links, etc.).

Users with permissions (namely current exec), will be able to access the CMS by either heading to `/cms`, or clicking on the pencil icon that shows in the bottom right when logged in, and clicking on "Go to Website Editor".

Creating new pages can be done within the "Pages" tab of the CMS. The "Snippets" area is used to manage the following:
- Social media - add links to new social media on the home page and in the footer. Icons are from FontAwesome 5 - use the classes for that icon and add them into the icon field.
- Event types - types for event. Can be in one of 4 "categories" - Academic, Gaming, Social, Society. Event types can also have unique background pages on the event page and on the event cards on the home page
- Footer links - add links to internal/external links in the footer (displayed on the right hand side)
- Sponsors - add details of sponsors here for display on the home page and in sidebars. **This does not populate sponsors on the `/sponsors` page**. Also provide normal and "dark mode" versions of the sponsors logo for display.

Note that some pages across the site are not editable within the CMS - for example, this includes all account pages, the home page and the report page. These are editable in the corresponding templates within the repository.