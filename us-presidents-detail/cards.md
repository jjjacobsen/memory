# U.S. Presidents - Detail - Improved Card Template

One card template that gives a fact or accomplishment and asks which president it belongs to

## 1. Detail to Name

### Front

```html
<div class=question>Which president {{Detail}}</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=name>{{Name}}</div>
{{#Extra}}
<div class=extra><em>{{Extra}}</em></div>
{{/Extra}}
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

.question {
  font-size: 1.05em;
}

.name {
  font-size: 1.4em;
  font-weight: 700;
  margin-bottom: 0.25em;
}

.extra {
  font-size: 0.95em;
  color: #57606a;
}

.card.nightMode .extra,
.nightMode .card .extra {
  color: #9aa4ae;
}
```

## Notes

- The Extra field only renders when it has content, kept through the conditional block
- Extra stays in italics as before, but now reads as a muted secondary line
- The president name is the large bold element so the answer leads
- Night mode softens the extra text so it stays readable on a dark background
