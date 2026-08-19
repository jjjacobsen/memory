# Basic - Improved Card Templates

One card template that shows a prompt on the front and the answer on the back

## 1. Front to Back

### Front

```html
{{Front}}
```

### Back

```html
{{FrontSide}}

<hr id=answer>

{{Back}}
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
```

## Notes

- Front shows only `Front` exactly as stored, so field HTML still renders
- Back shows the front side, the styled divider, then `Back`
- The base styling is shared with every other note type so all cards look consistent
- Night mode restyles the card and the divider automatically
