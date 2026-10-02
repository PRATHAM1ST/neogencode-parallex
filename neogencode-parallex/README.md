# Pratham — a different perspective

A responsive portfolio and parallax example made with **only HTML and CSS**. Open `index.html` in a browser. No installation or build step is required.

## Explain it in your coding round

The effect lives in `.parallax` in `styles.css`:

```css
.parallax {
  position: relative;
  isolation: isolate;
  clip-path: inset(0);
}
.parallax::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: -1;
  background: url("assets/mountains.jpg") center / cover;
}
@media (prefers-reduced-motion: reduce) {
  .parallax::before { position: absolute; }
}
```

The `::before` pseudo-element provides an image layer anchored to the viewport with `position: fixed`. `clip-path: inset(0)` limits that layer to the section’s visible area, and `isolation: isolate` keeps it behind the section’s content. As the section scrolls, it reveals different parts of the stationary image, creating depth. `cover` fills the layer without distorting the image. The actual page adds a dark gradient for readable text.

This works on desktop and touch devices without relying on mobile support for `background-attachment: fixed`. When reduced motion is preferred, the layer switches to `position: absolute` and moves with its section, removing the parallax effect.

## Included

- Two mountain parallax sections.
- Three featured project covers and all 13 unique supplied links.
- Native radio buttons filter the project directory using CSS `:checked` and sibling selectors. Keyboard users can focus the group with Tab and select categories with the arrow keys.
- A native `<details>` panel explains the effect.
- Mobile layout, skip link, visible keyboard focus, and reduced motion support.
- Each external project opens in a new tab.

SP Plast and Mamta Design Co. use their sites’ actual social preview images. Pratham’s portfolio has an original CSS graphic cover, not a website screenshot. Image sources are documented in `assets/SOURCES.md`. Google Fonts is optional; system fonts are used if it is unavailable. All photographs and preview images are saved locally so the page works offline.

## Files

- `index.html` — content and links
- `styles.css` — presentation, parallax, and category filters
- `assets/` — landscape photograph and its source credit

There is no JavaScript, framework, tracking, backend, or build dependency.

## Check the content

Run `python verify.py` to verify every supplied project URL, category counts, local assets, and the absence of JavaScript. Browser checks also covered filtering, the expandable explanation, narrow layouts, and reduced motion.
