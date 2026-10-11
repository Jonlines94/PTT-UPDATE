# PTT Solutions – site update

Redesigned site for PTT Solutions Limited (two-way radio equipment, Burnham-On-Crouch). Black and champagne-gold design built around the original site's photos and copy, with Apple-style scroll effects.

## Use it
Open `index.html` in a browser, or host it as-is (GitHub Pages, any web server). It is one self-contained file: CSS, JavaScript and photos are all inlined.

## Repo layout
| Path | What it is |
| --- | --- |
| `index.html` | The finished, built site. |
| `src/template.html` | Editable source (images appear as `{{IMG:name}}` placeholders). |
| `assets/images/` | The original site's photos (converted from AVIF to JPEG), the original logo, and the favicon files. |
| `build.py` | Rebuilds `index.html` from the template and images. |

To change anything: edit `src/template.html` (or swap a photo in `assets/images/` keeping the same file name), then run `python3 build.py`.

## What's in the page
- Pinned hero with zoom and fade, then a word-by-word statement.
- Pinned services section that changes image as you scroll.
- Horizontal sector gallery driven by vertical scroll.
- Count-up key figures, filterable shop preview, FAQ, enquiry form.
- Phones, tablets, short laptop screens and "reduce motion" fall back to a normal scrolling layout.
- Keyboard and screen-reader friendly, with a no-JavaScript fallback, LocalBusiness structured data and a favicon.

## Before going live
- **Forms:** the enquiry forms open the visitor's email app (`mailto:`). Connect a form service or backend for real submissions.
- **Shop:** a selection of products with enquiry buttons; real checkout needs a shop platform. Prices are exclusive of VAT, shipping £8.95 per order, as on the original site.
- **Fonts:** Raleway loads from Google Fonts when online and falls back to a system font otherwise.
- **Photos:** most original photos are small thumbnails, so they are shown at modest sizes. Higher-resolution versions would look sharper.
- **Logo and favicon:** the header and footer use your original logo (white-on-transparent version in `assets/images/logo.png`, made from the 181 px original in `original-logo.png`). A larger original logo file would look sharper. The favicon files (`favicon-32.png`, `favicon-64.png`, `apple-touch-icon.png`, `favicon.png`) are built from the bars icon in that logo, because the original favicon file wasn't in the supplied zip. To use the real one, replace those files (keep the names) and run `python3 build.py`.
