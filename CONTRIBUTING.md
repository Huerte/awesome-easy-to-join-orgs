# Contributing

## Who can contribute

Anyone. Beginners, experienced developers, students, and people who do not code. If you know an organization that is easy to join, you can add it here. You do not need to know how Git works.

## What belongs on the list

Organizations on GitHub that you can join without coding. For most of them you open an issue, someone accepts you, and you are in. A short form or a simple request process counts too.

If an organization asks for a coding test or a long application, it does not belong here.

## Add an organization without code

1. Open a [new issue](../../issues/new/choose) and pick "Add an organization"
2. Paste the link to the organization
3. Tell us how people join (an issue in one of its repos, a form, an email)

That is all. Someone will add it to the list for you.

## Add an organization with a pull request

1. Fork this repo with the Fork button at the top right
2. Clone your fork and create a branch

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   git checkout -b add-org-name
   ```

3. Open `README.md` and add one row to the table, in alphabetical order

   ```markdown
   | <img src="https://github.com/org-name.png?size=40" width="40" height="40" alt="Org Name"> | Org Name | One short line about what it does | [Visit Org](https://github.com/org-name) |
   ```

   Copy a row that is already there and replace the name, the description and the org handle everywhere they appear. Keep the description to one short line, in your own words or taken from the org's About text.

   Descriptions refresh every week from each organization's About text on GitHub. If the organization has no About text, yours stays. To keep your own wording for good, add `<!-- keep -->` at the end of your description.

4. Commit and push

   ```bash
   git add README.md
   git commit -m "Add Org Name"
   git push origin add-org-name
   ```

5. Go to your fork on GitHub and click "Compare & pull request"

Never opened a pull request before? Start with [First Contributions](https://github.com/firstcontributions/first-contributions) or watch [this walkthrough](https://youtu.be/WldXhauP024).

## Rules for the list

- One row per organization
- Link to the organization's GitHub page, with no tracking parameters
- Keep the table in alphabetical order by organization name
- Keep the description on one line, with no `|` characters
- Check that the link works before you submit

## Fixing or removing an entry

If an organization stopped accepting people or a link is dead, open an issue or delete the row in a pull request.

## Need help?

Stuck on anything? Ask in the comments of your issue or pull request. Basic questions are fine.

If this list helped you, a [star](https://github.com/Huerte/awesome-easy-to-join-orgs) helps other people find it. It is optional, and you do not need it to contribute.
