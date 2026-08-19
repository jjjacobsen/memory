# Linux Sys Admin - Improved Card Template

One card template that shows a concept and asks you to recall its meaning

## 1. Concept to Meaning

### Front

```html
<div class=concept>{{Concept}}</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div id=meaning class=meaning>{{Meaning}}</div>
<script>
(() => {
  const el = document.getElementById(`meaning`);
  el.innerHTML = el.textContent.replace(/;\s*/g, `<br>`);
})();
</script>
```

## Styling

```css
.card {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
  font-size: 20px;
  line-height: 1.5;
  text-align: center;
  padding: 1em;
  color: #1f2328;
  background-color: #ffffff;
}

.card.nightMode,
.nightMode .card {
  color: #e6e6e6;
  background-color: #1e1e1e;
}

hr#answer {
  width: 60%;
  max-width: 480px;
  height: 2px;
  margin: 1.2em auto;
  border: none;
  background: linear-gradient(to right, rgba(79, 111, 159, 0), #4f6f9f, rgba(79, 111, 159, 0));
}

.card.nightMode hr#answer,
.nightMode .card hr#answer {
  background: linear-gradient(to right, rgba(122, 151, 191, 0), #7a97bf, rgba(122, 151, 191, 0));
}

.concept {
  font-size: 1.15em;
  font-weight: 700;
}

.meaning {
  text-align: left;
  max-width: 36em;
  margin: 0 auto;
  line-height: 1.6;
}
```

## Notes

- The script turns each `;` in the Meaning field into a line break, so definitions read as separate lines
- The old dead newline replacement was removed, only the `;` rule remains
- The meaning is left aligned and width capped for comfortable reading of longer definitions
- The concept stays visible above the divider and is emphasized
