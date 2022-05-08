# A collection of half started projects and code snippets. Make work faster or learn new techniques.

## Step one organize all projects.

### Outline

Plan, design and execute on websites reflecting the skils on my resume.

Project 3 - Site that provides data for Liberty City/Model City

Project 4 - Favorite Miami Restaurant

Project 5 - Favorite Miami Hotel 

What program do you want to co-write together?

> HTML CSS AND Javascript to start.
> Goal make a website that utilizes everything in diverse snippets of code.

> Deadline 2023

# WAI-ARIA marking guide

The aim of these tasks is to demonstrate an understanding of the techniques covered in the [WAI-ARIA Basics](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/WAI-ARIA_basics) lesson in Learn Web Development on MDN.

## Task 1

In our first ARIA task, we present you with a section of non-semantic markup, which is obviously meant to be a list. Assuming you are not able to change the elements used, how can you allow screenreader users to recognize this as a list? 

The `list` and `listitem` roles are what you need here. The updated markup would look like so:

```
<div role="list">
  <div role="listitem">Pig</div>
  <div role="listitem">Gazelle</div>
  <div role="listitem">Llama</div>
  <div role="listitem">Majestic moose</div>
  <div role="listitem">Hedgehog</div>
</div>
```

## Task 2

In our second WAI-ARIA task, we present a simple search form, and we want you to add in a couple of WAI-ARIA features to improve its accessibility:

1. How can you allow the search form to be called out as a separate landmark on the page by screenreaders, to make it easily findable?
2. How can you give the search input a suitable label, without explicitly adding a visible text label to the DOM?

Answers:

1. Give the `<form>` element a `role="search"`. Most screenreaders will explicitly call this out as a search form, and/or include it as a separate landmark in the page's landmarks list.
2. Include label text inside an `aria-label=""` attribute on the `<input>` element. This way it won't be visible on the page, but it will be read out by screenreaders.

The finished HTML should look something like this:

```
<form role="search">
  <input type="search" name="search"
    aria-label="Search for your favorite content on our site">
</form>
```

## Task 3
For this final WAI-ARIA task, we return to an example we previously saw in the [CSS and JavaScript skilltest](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/CSS_and_JavaScript/Test_your_skills:_CSS_and_JavaScript_accessibility). As before, we have a simple app that presents a list of animal names. Clicking one of the animal names causes a further description of that animal to appear in a box below the list. Here, we are starting with a mouse- and keyboard-accessible version.  

The problem we have now is that when the DOM changes to show a new decription, screenreaders cannot see what has changed. Can you update it so that description changes are annouced by the screenreader?

There are two ways to solve this:

* Add an `aria-live=""` attribute to the animal-description `<div>` to turn it into a live region, so when its content changes, the updated content will be read out by a screenreader. The best value is probably `assertive`, which makes the screenreader read out the updated content as soon as it changed. `polite` means that the screenreader will wait until other descriptions have finished before it starts reading out the changed content.
* Add a `role="alert"` attribute to the animal-description `<div>`, to make it have alert box semantics. This has the same effect on the screenreader as setting `aria-live="assertive"` on it.


# CSS and JS accessibility marking guide

The aim of these tasks is to demonstrate an understanding of the techniques covered in the [CSS and JavaScript accessibility best practices](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/CSS_and_JavaScript) lesson in Learn Web Development on MDN.

## Task 1

In the first task you are presented with a list of links. However, their accessibility is pretty bad — there is no way to really tell that they are links, or to tell which one the user is focussed on.

We'd like you to assume that the existing ruleset with the `a` selector is supplied by some CMS, and that you can't change it — instead, you need to create new rules to make the links look and behave like links, and for the user to be able to tell where they are in the list.

The CSS could look something like this:

```
li a {
  text-decoration: underline;
  color: rgb(150,0,0);
}

li a:hover, li a:focus {
  text-decoration: none;
  color: rgb(255,0,0);
}
```

## Task 2

In this next task you are presented with a simple bit of content — just headings and paragraphs. There are  accessibility issues with the colors and sizing of the text; we'd like you to:

1. Explain what the problems are, and what the guidelines are that state the acceptable values for color and sizing.
2. Select new values for the color and font-size that fix the problem.
3. Update the CSS with these new values to fix the problem.
4. Test the code to make sure the problem is now fixed. Explain what tools or methods you used to select the new values and test the code.

The answers:

1. (Q1) The problems are that first of all, the color contrast is not acceptable, as per WCAG criteria [1.4.3 (AA)](https://www.w3.org/TR/WCAG21/#contrast-minimum) and [1.4.6 (AAA)](https://www.w3.org/TR/WCAG21/#contrast-enhanced), and secondly, the text is sized using vw units, which means that it is not zoomable in most browsers. [WCAG 1.4.4 (AA)](https://www.w3.org/TR/WCAG21/#resize-text) states that text should be resizable.
2. (Qs 2 and 3) to fix the code, you need to
  * Choose a much better contrasting set of background and foreground colors.
  * Use some different units to size the text (such as rem or even px), or even implement something that uses a combination of vw and other units, if you want it resizable but still relative in part to the viewport size
3. For testing:
  * You can test color contrast using a tool such as [aXe](https://www.deque.com/axe/), The [Firefox Accessibility Inspector](https://developer.mozilla.org/en-US/docs/Tools/Accessibility_inspector), or even a simple standalone web page tool like the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/). 
  * For text resizing, you'd need to load the example in a browser and try to resize it. Resizing vw unit-sized text works in Safari, but not Firefox or Chromium-based browsers.

For the updated code, something like this would work for the updated color scheme:

```
main {
  padding: 20px;
  background-color: red;
}

h1, h2, p {
  color: black;
}
``` 

And something like this would work for the font sizing:

```
h1 {
  font-size: calc(2.5rem);
}

h2 {
  font-size: calc(2rem);
}

p {
  font-size: calc(1.2rem);
}
```

Or this, if you want to do something a bit cleverer that gives you resizable viewport-relative units: 

```
h1 {
  font-size: calc(1.5vw + 1rem);
}

h2 {
  font-size: calc(1.2vw + 0.7rem);
}

p {
  font-size: calc(1vw + 0.4rem);
}
```

## Task 3

In our final task here, you have some JavaScripting to do. We have a simple app that presents a list of animal names. Clicking one of the animal names causes a further description of that animal to appear in a box below the list.

But it is not very accessible — in its current state you can only operate it with the mouse. We'd like you to add to the HTML and JavaScript to make it keyboard acessible too.

Answers:

1. To begin with, you'll need to add `tabindex="0"` to the list items to make them focusable via the keyboard.
2. Then you'll need to add in another event listener inside the `forEach()` loop, to make the code respond to keys being pressed while the list items are selected. It is probably a good idea to make it respond to a specific key, such as "Enter", in which case something like the following is probably acceptable:

```
item.addEventListener('keyup', function(e) {
  if(e.key === 'Enter') {
    handleSelection(e);
  }
});
```

# HTML accessibility marking guide

The aim of these tasks is to demonstrate an understanding of the techniques covered in the [HTML: A good basis for accessibility](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML) lesson in Learn Web Development on MDN.

## Task 1

In this task we will test your understanding of text semantics, and why they are good for accessibility. You don't need to worry too much about recreating the _exact_ same look and text sizing, as long as the semantics are good.

The given text is a simple information panel with action buttons:

```
<font size="7">Need help?</font>
<br><br>
If you have any problems with our products, our  support center can offer you all the help you need, whether you want:
<br><br>
1. Advice choosing a new product
<br>
2. Tech support on an existing product
<br>
3. Refund and cancellation assistance
<br><br>
<font size="5">Contact us now</font>
<br><br>
Our help center contains live chat, e-mail addresses, and phone numbers.
<br><br>
<div class="button">Find Contact Details</div>
<br><br>
<font size="5">Find out answers</font>
<br><br>
Our Forums section contains a large knowledge base of searchable previously asked questions, and you can always ask a new question if you can't find the answer you're looking for.
<br><br>
<div class="button">Access forums</div>
```

But of course, this is terrible for semantics and accessibility. A much better set of markup would look like so:

```
<h2>Need help?</h2>

<p>If you have any problems with our products, our  support center can offer you all the help you need, whether you want:</p>
<ul>
  <li>Advice choosing a new product</li>
  <li>Tech support on an existing product</li>
  <li>Refund and cancellation assistance</li>
</ul>
<h3>Contact us now</h3>

<p>Our help center contains live chat, e-mail addresses, and phone numbers.</p>

<button>Find Contact Details</button>

<h3>Find out answers</h3>

<p>Our Forums section contains a large knowledge base of searchable previously asked questions, and you can always ask a new question if you can't find the answer you're looking for.</p>

<button>Access forums</button>
```

You can get a couple of extra marks for:

1. Just using `<button>`, not `<button class="button">` (repeating semantics is unnecessary), and updating the CSS selector to make sure the button still picks up the styles
2. Using an unordered list, not an ordered list — the list of items doesn't really need to be in any order.

## Task 2
In the second task, you have a form containing three input fields. You need to:

1. Semantically associate the input with their labels.
2. Assume that these inputs will be part of a larger form, and wrap them in an element that associates them all together as a single related group.
3. Give the group a description/title that summarises all of the information as personal data.

This is fairly simple, especially if you have previously worked through our [Web forms](https://developer.mozilla.org/en-US/docs/Learn/Forms) module. You need to:

1. Use `<label>` elements and `id`s to associate labels with inputs.
2. Use a `<fieldset>` to associate the elements together as one group.
3. Use a `<legend>` to give the `<fieldset>` a description/title.

Your answer should end up looking something like this:

```
<form>
  <fieldset>
  <legend>Personal data</legend>
    <ul>
      <li>
        <label for="name">Name</label>
        <input type="text" name="name" id="name">
      </li>
      <li>
        <label for="age">Age</label>
        <input type="number" name="age" id="age">
      </li>
      <li>
        <label for="email">Email address</label>
        <input type="email" name="email" id="email">
      </li>
    </ul>
  </fieldset>
</form>
```

# Task 3

In this task you are required to turn all the information links in the paragraph into good, accessible links.

1. The first two links just go to regular web pages.
2. The third link goes to a PDF, and it's large — 8MB.
3. The fourth link goes to a Word document, so the user will need some kind of application installed that can handle that.

Initially the paragraph looks like this:

```
<p>For more information about our activities, check out our fundraising page (<a href="/fundraising">click here</a>), education page (<a href="/education">click here</a>), sponsorship pack (<a href="/resources/sponsorship.pdf">click here</a>), and assessment sheets (<a href="/resources/assessments.docx">click here</a>).</p>
```

But you should update it to something like this:

```
<p>For more information about our activities, check out our <a href="/fundraising">fundraising page</a>, <a href="/education">education page</a>, <a href="/resources/sponsorship.pdf">sponsorship pack (PDF, 8MB)</a>, and <a href="/resources/assessments.docx">assessment sheets (Word document)</a>.</p>
```

## Task 4

In our final HTML accessibility task, you are given a simple image gallery, which has some accessibility problems. Can you fix them?

1. The header image has an accessiiblity issue, and so do the gallery images.
2. You could take the header image further and implement it using CSS for better accessibility. Why is this better, and what would a solution look like?

So, on to the answers:

1. The header image is decorative, so doesn't really need alt text. The best solution if you are going to use decorative HTML images is to put `alt=""`, so a screenreader will just read out nothing — rather than a descrition, or the image file name. It is not part of the content. 
2. The gallery images need alt text, and they are part of the content. The updated HTML could look something like this:

```
<header>
  <img src="images/star.png" alt="">
  <h1>Groovy images</h1>
</header>
<main>
  <img src="images/teapot.jpg" alt="a black teapot placed on a shelf just inside a window">
  <img src="images/football.jpg" alt="A black and white round panelled ball">
</main>
```

3. It would be arguable better to implement the background header image using CSS background images. To do this, you would remove the following line:

```
<img src="images/star.png" alt="A star that I use to decorate my page">
```

And add in a CSS rule along these lines:

```
h1 {
  background: url(images/star.png) no-repeat left;
  padding-left: 50px;
}
```

# Marking guide for "Fundamental Layout Comprehension"

The following guide outlines a marking guide for the MDN Learning Area CSS Layout Topic. Each subtask detailed in the assessment is listed below, along with an explanation of how many marks the task is worth, and the mark breakdown.

Note: These are guidelines, not set in stone rules — you are of course free to use your judgement on mark awarding when you meet an edge case, or somethign that isn't clearly cut.

The overall mark awarded is out of 25. Work out their final mark, and then divide by 25 and multiply by 100 to give a percentage mark. For reference, you can find a finished example in this folder that would be awarded top marks.

While the actual amount of code that is required to be added is relatively small, this task is about making the right choices for this layout.

**Display the navigation items in a row, with an equal amount of space between the items.**

Here the student should use flexbox, adding `display: flex` to `nav ul` (2 marks), and `justify-content: space-between` (2 marks) to distribute the additional space between the items.  

**The navigation bar should scroll with the content and then become stuck at the top of the viewport when it reaches it.**

The selector `nav` should have `position: sticky` (2 marks) plus an offset value of `top: 0` (2 marks). 

**The image that is inside the article should have text wrapped around it.**

The image should be floated left `float: left` (2 marks) with a right and bottom margin to move the text away from it (3 marks).

**The `<article>` and `<aside>` elements should display as a two column layout. The columns should be a flexible size so that if the browser window shrinks smaller the columns become narrower.**

Here the student would ideally use CSS Grid  `display: grid` (2 marks), with the `fr` unit for the columns `grid-template-columns: 3fr 1fr` (2 marks). It would also be possible to use flexbox, and that would be acceptable too. Percentages would work for the column tracks, but ideally they realise that the fr unit works nicely here. The actual proportions they pick don't really matter. A `grid-gap` or `gap` property should separate the tracks, e.g. `grid-gap: 20px` (2 marks).

**The photographs should display as a two column grid with a 1 pixel gap between the images.**

This should be grid layout, a flex layout would mean the last image would spread out across the two tracks. A grid layout with two 1fr tracks (4 marks) will get the display we want with a `grid-gap` of 1px (2 marks). In supporting browsers the `gap` property rather than `grid-gap` will work.
