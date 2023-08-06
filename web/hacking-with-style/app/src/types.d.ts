export { }

declare module 'express-session' {
  interface SessionData {
    user?: {
      username: string
      password: string
      isAdmin: boolean
    }
  }
}
