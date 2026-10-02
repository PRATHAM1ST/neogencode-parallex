# Pratham — a different perspective

A responsive portfolio and parallax example made with **only HTML and CSS**. Open `index.html` in a browser. No installation or build step is required.

## Explain it in your coding round

The effect lives in `.parallax` in `styles.css`:

```css
.parallax {
  background-image: url("assets/mountains.jpg");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}
```

`background-attachment: fixed` anchors the background to the viewport. The page content moves while the image stays still, creating the illusion of depth. `cover` fills the section without distorting the image. The actual page layers a subtle dark gradient over the photo to keep the text readable.

Touch devices use `background-attachment: scroll` because mobile browsers handle fixed backgrounds inconsistently. The same fallback respects `prefers-reduced-motion`. The page is fully usable in either mode.

## Included

- Two mountain parallax sections.
- Three featured project covers and all 13 unique supplied links.
- Native radio buttons filter the project directory using CSS `:checked` and sibling selectors. Keyboard users can focus the group with Tab and select categories with the arrow keys.
- A native `<details>` panel explains the effect.
- Mobile layout, skip link, visible keyboard focus, and reduced motion support.
- Each external project opens in a new tab.

SP Plast and Mamta Design Co. use their sites’ actual social preview images. AG Project has an original CSS graphic cover, not a website screenshot. Image sources are documented in `assets/SOURCES.md`. Google Fonts is optional; system fonts are used if it is unavailable. All photographs and preview images are saved locally so the page works offline.

## Files

- `index.html` — content and links
- `styles.css` — presentation, parallax, and category filters
- `assets/` — landscape photograph and its source credit

There is no JavaScript, framework, tracking, backend, or build dependency.

## Check the content

Run `python verify.py` to verify every supplied project URL, category counts, local assets, and the absence of JavaScript. Browser checks also covered filtering, the expandable explanation, narrow layouts, and reduced motion.
