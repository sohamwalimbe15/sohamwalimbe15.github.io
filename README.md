# Personal academic website

Plain HTML, CSS and a few lines of JS. No build step.

Files: `index.html` (all content), `style.css`, `script.js`, `academic_cv.pdf` (the "Download CV" button), `check.py` (smoke check). Optional: `photo.jpg` (the photo hides itself if missing).

## Publish on GitHub Pages

1. On GitHub, create a **public** repository named exactly `Sohamwalimbe.github.io` (no README, no .gitignore, no license).
2. In this folder, run:

   ```sh
   python3 check.py
   git init -b main
   git add index.html style.css script.js academic_cv.pdf check.py README.md
   git add photo.jpg   # only if you added one
   git commit -m "Initial website"
   git remote add origin https://github.com/Sohamwalimbe/Sohamwalimbe.github.io.git
   git push -u origin main
   ```

   `academic_cv.tex` is not needed by the site. Add it too if you want it in the repo.
3. On GitHub: **Settings → Pages → Build and deployment**. Set Source to **Deploy from a branch**, Branch to **main**, folder to **/ (root)**, then Save.
4. After a minute or two the site is live at <https://sohamwalimbe.github.io>.

## Update content later

- Edit `index.html` (each section is marked by its `id`), then update the date in the footer.
- If the CV changes, replace `academic_cv.pdf` with the new export.
- **Placeholder links:** every link with `data-todo` (Google Scholar and each project's GitHub link) is inert. To activate one, set its real URL in `href` and delete the `data-todo="..."` attribute.
- **Photo:** save a square image as `photo.jpg` next to `index.html`.
- Check and publish:

  ```sh
  python3 check.py
  git add -A && git commit -m "Update site" && git push
  ```
