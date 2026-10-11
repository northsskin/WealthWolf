-- Already applied to the shared project. Kept here so the database can be
-- recreated, and so schema changes are reviewed like code.

-- One row per player: their whole progress as JSON, synced from the app.
create table public.progress (
  user_id uuid primary key references auth.users (id) on delete cascade,
  progress jsonb not null,
  profile jsonb not null default '{}'::jsonb,
  rev text not null,
  updated_at timestamptz not null default now()
);

alter table public.progress enable row level security;

-- Players can only see and change their own row.
create policy "Players read their own progress" on public.progress
  for select to authenticated using ((select auth.uid()) = user_id);
create policy "Players create their own progress" on public.progress
  for insert to authenticated with check ((select auth.uid()) = user_id);
create policy "Players update their own progress" on public.progress
  for update to authenticated using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
create policy "Players delete their own progress" on public.progress
  for delete to authenticated using ((select auth.uid()) = user_id);

grant select, insert, update, delete on public.progress to authenticated;
revoke all on public.progress from anon;
