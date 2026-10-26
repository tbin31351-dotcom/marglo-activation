# marglo-activation (GitHub "server")

`activated.txt` = list of activated Device IDs. The app downloads it from
`raw.githubusercontent.com` and opens only if the user's HWID is inside.

## One-time setup
1. GitHub -> New repository -> name `marglo-activation` -> **Public** (raw links of private repos need a token) -> create.
2. Upload all files of this folder (keep `.github/workflows/activate.yml`).
3. In the Android project, `app/src/main/assets/dialog.conf`:
   `activation_url=https://raw.githubusercontent.com/<YOUR_USER>/marglo-activation/main/activated.txt`
4. Repo -> Settings -> Actions -> General -> Workflow permissions -> **Read and write permissions** -> Save.

## Activate a user
- **Easiest (phone/web):** repo -> Actions -> *Activate / Revoke HWID* -> Run workflow -> action `add`, paste HWID, note -> Run.
- **Manual:** open `activated.txt` on GitHub -> pencil icon -> add a line `A1B2-C3D4-E5F6-0789  # Ali` -> Commit.
- **Termux/PC:** `python manage.py add A1B2-C3D4-E5F6-0789 "Ali"` then `git commit -am up && git push`.

## Revoke
Run the workflow with `remove`, or delete the line.

## Notes
- GitHub raw caches for ~5 minutes: a new activation may take up to ~5 min to reach the app (user taps *Check Activation* again).
- The file is public: anyone can see the HWIDs (they are hashed IDs, not personal data). Don't put names/phone numbers in notes.
- Need instant activation / private list / per-user expiry? Move to your own server using the `{HWID}` mode in `dialog.conf`.
