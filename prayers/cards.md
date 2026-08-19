# Prayers - Improved Card Templates

Two card templates that test recall from prayer name to prayer text and the reverse

## 1. Prayer Name to Prayer Text

### Front

```html
<div class=prayer-title>{{Front}}</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=prayer-text id=card1-prayer>{{Back}}</div>
<script>
(() => {
  const el = document.getElementById(`card1-prayer`);
  el.innerHTML = el.textContent.replace(/;;/g, `<br><br>`).replace(/;\s*/g, `<br>`);
})();
</script>
```

## 2. Prayer Text to Prayer Name

### Front

```html
<div class=prayer-text id=card2-prayer>{{Back}}</div>
<script>
(() => {
  const el = document.getElementById(`card2-prayer`);
  el.innerHTML = el.textContent.replace(/;;/g, `<br><br>`).replace(/;\s*/g, `<br>`);
})();
</script>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=prayer-title>{{Front}}</div>
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

.prayer-title {
  font-size: 1.2em;
  font-weight: 600;
}

.prayer-text {
  font-family: Georgia, Palatino, Times, serif;
  font-size: 1.05em;
  line-height: 1.7;
  text-align: left;
  max-width: 34em;
  margin: 0 auto;
}
```

## Notes

- The script turns `;;` into a blank line and `;` into a line break inside the prayer text
- The prayer body uses a readable serif face, left aligned, with a width cap so lines stay short
- The two distinct element ids keep each template self contained
- The reverse card shows the prayer text as the prompt and the name as the answer
