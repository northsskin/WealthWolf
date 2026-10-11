import { getApp, getApps, initializeApp } from 'firebase/app'
import { connectAuthEmulator, getAuth } from 'firebase/auth'
import { getFirestore } from 'firebase/firestore'

// Firebase settings come from .env.local (see .env.example). `npm run dev:emu`
// instead points sign-in at the local Auth emulator under a demo project, so
// accounts can be tested without a real Firebase project.
const env = import.meta.env

export const usingEmulators = env.VITE_USE_EMULATORS === '1'

const config = usingEmulators
  ? { apiKey: 'demo-key', authDomain: 'demo-wealthwolf.firebaseapp.com', projectId: 'demo-wealthwolf', appId: 'demo-app' }
  : {
      apiKey: env.VITE_FIREBASE_API_KEY,
      authDomain: env.VITE_FIREBASE_AUTH_DOMAIN,
      projectId: env.VITE_FIREBASE_PROJECT_ID,
      storageBucket: env.VITE_FIREBASE_STORAGE_BUCKET,
      messagingSenderId: env.VITE_FIREBASE_MESSAGING_SENDER_ID,
      appId: env.VITE_FIREBASE_APP_ID,
    }

// False until the Firebase settings are filled in: sign-in can't work yet.
export const configured = usingEmulators || Boolean(config.apiKey && config.projectId && config.appId)

const app = configured ? (getApps().length ? getApp() : initializeApp(config)) : null

export const auth = app ? getAuth(app) : null
if (auth && usingEmulators && !auth.emulatorConfig) {
  connectAuthEmulator(auth, 'http://127.0.0.1:9099', { disableWarnings: true })
}

// There's no Firestore emulator here (it needs Java), so emulator mode keeps
// "the cloud copy" in a local stand-in instead; see lib/sync.js.
export const db = app && !usingEmulators ? getFirestore(app) : null
