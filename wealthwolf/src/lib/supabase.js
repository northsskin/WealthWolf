import { createClient } from '@supabase/supabase-js'

// Supabase settings come from .env (the shared project) or .env.local (an
// override). The publishable key is meant to be public: row-level security on
// the progress table is what keeps each player's data to themselves.
export const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
export const supabaseKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY

// False until the Supabase settings are filled in: sign-in can't work yet.
export const configured = Boolean(supabaseUrl && supabaseKey)

export const supabase = configured
  ? createClient(supabaseUrl, supabaseKey, {
      auth: { flowType: 'pkce', persistSession: true, autoRefreshToken: true, detectSessionInUrl: true },
    })
  : null
