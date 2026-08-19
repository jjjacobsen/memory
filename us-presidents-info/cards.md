# U.S. Presidents - Info - Improved Card Templates

Seven card templates that test number, name, term, party, portrait, and state, one question type each

## 1. Name to Number

### Front

```html
<div class=question>What number president was {{Name}}</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=answer>{{Number}}</div>
```

## 2. Number to Name

### Front

```html
<div class=question>Who was president {{Number}}?</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=name>{{Name}}</div>
```

## 3. Name to Term

### Front

```html
<div class=question>What were the years {{Name}} was in office?</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=answer>{{Term}}</div>
```

## 4. Term to Name

### Front

```html
<div class=question>Who was president from {{Term}}?</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=name>{{Name}}</div>
```

## 5. Name to Party

### Front

```html
<div class=question>What political party did {{Name}} belong to?</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=answer>{{Party}}</div>
```

## 6. Portrait to Name

### Front

```html
<div class=question>Who is this?</div>

<div class=portrait>
{{Portrait}}
</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=name>{{Name}}</div>
```

## 7. Name to State

### Front

```html
<div class=question>What state did {{Name}} represent?</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=answer>{{State}}</div>
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
}

.card.nightMode .question,
.nightMode .card .question {
  color: #9aa4ae;
}

.answer {
  font-size: 1.15em;
  font-weight: 600;
}

.name {
  font-size: 1.4em;
  font-weight: 700;
}

.portrait img {
  max-width: 220px;
  max-height: 300px;
  border-radius: 0.5em;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}
```

## Notes

- All seven templates are preserved exactly as before, only the presentation changed
- Name answers render large and bold, numeric and factual answers render medium and bold
- The portrait sits alone on its own line so the image field renders as an image, with a subtle frame
- Questions share a muted tone so each answer stands out clearly
- Cards can be enabled or disabled independently in Anki
