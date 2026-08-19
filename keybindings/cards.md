# Keybindings - Improved Card Templates

Two card templates that test recall of the key sequence and of the effect, each using the same three fields

## 1. Program and Effect to Binding

### Front

```html
<div class=kv><span class=label>Program</span><span class=value>{{Program}}</span></div>
<div class=kv><span class=label>Effect</span><span class=value>{{Effect}}</span></div>
<div class=question>What is the keybinding?</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=binding>{{Binding}}</div>
```

## 2. Program and Binding to Effect

### Front

```html
<div class=kv><span class=label>Program</span><span class=value>{{Program}}</span></div>
<div class=kv><span class=label>Binding</span><span class=value><span class=binding>{{Binding}}</span></span></div>
<div class=question>What does this keybinding do?</div>
```

### Back

```html
{{FrontSide}}

<hr id=answer>

<div class=answer>{{Effect}}</div>
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

.kv {
  margin: 0.5em 0;
}

.label {
  display: inline-block;
  min-width: 5.5em;
  margin-right: 0.6em;
  font-size: 0.8em;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #57606a;
}

.card.nightMode .label,
.nightMode .card .label {
  color: #9aa4ae;
}

.binding {
  display: inline-block;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 1.1em;
  font-weight: 600;
  padding: 0.3em 0.7em;
  border: 1px solid #c8ccd1;
  border-bottom-width: 3px;
  border-radius: 0.35em;
  background: #f6f8fa;
  color: #1f2328;
  margin: 0.1em;
}

.card.nightMode .binding,
.nightMode .card .binding {
  background: #2b2f36;
  border-color: #4a4f57;
  color: #e6e6e6;
}

.question {
  margin-top: 1.4em;
  font-weight: 600;
}

.answer {
  font-size: 1.1em;
  font-weight: 600;
}
```

## Notes

- Card 1 tests recall from effect to binding, card 2 tests recall from binding to effect
- Bindings render in a monospace key-cap style so key sequences stand out
- Binding values like `<C-b> c` are kept inline inside tags so they display literally
- The base styling matches every other note type for a consistent look
