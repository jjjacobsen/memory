# Quotes - Improved Card Template

One card template that shows a quote and asks who said it

## 1. Quote to Name

### Front

```html
<div class=question>Who said the following?</div>

<div class=quote>&ldquo;{{Quote}}&rdquo;</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=attribution>{{Name}}</div>
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
  color: #57606a;
  margin-bottom: 1em;
}

.card.nightMode .question,
.nightMode .card .question {
  color: #9aa4ae;
}

.quote {
  font-family: Georgia, Palatino, Times, serif;
  font-size: 1.2em;
  font-style: italic;
  line-height: 1.6;
  max-width: 26em;
  margin: 0 auto;
}

.attribution {
  font-size: 1.1em;
  font-weight: 700;
}
```

## Notes

- The quote is wrapped in typographic quote marks by the template, the field stays clean
- The quote sits in a centered serif block with generous spacing
- The attribution is bold so the answer lands with clear hierarchy
- The question stays muted so the quote leads the card
