<script>
  import { APP_NAME } from "$lib/config.js";

  // Settings state
  let settings = $state({
    notifications: {
      emailNotifications: true,
      pushNotifications: false,
      weeklyReports: true,
      securityAlerts: true,
      marketingEmails: false,
    },
    privacy: {
      shareProfile: true,
      showOnlineStatus: false,
      allowDirectMessages: true,
      dataCollection: false,
    },
    appearance: {
      compactMode: false,
      showAnimations: true,
      highContrast: false,
      largeText: false,
    },
    security: {
      twoFactorAuth: false,
      sessionTimeout: true,
      loginAlerts: true,
      passwordExpiry: false,
    },
  });

  function saveSettings() {
    // In a real app, this would save to a backend
    console.log("Settings saved:", settings);
    // Show success message
    alert("Settings saved successfully!");
  }

  function resetSettings() {
    // Reset to defaults
    settings = {
      notifications: {
        emailNotifications: true,
        pushNotifications: false,
        weeklyReports: true,
        securityAlerts: true,
        marketingEmails: false,
      },
      privacy: {
        shareProfile: true,
        showOnlineStatus: false,
        allowDirectMessages: true,
        dataCollection: false,
      },
      appearance: {
        compactMode: false,
        showAnimations: true,
        highContrast: false,
        largeText: false,
      },
      security: {
        twoFactorAuth: false,
        sessionTimeout: true,
        loginAlerts: true,
        passwordExpiry: false,
      },
    };
  }
</script>

<svelte:head>
  <title>Settings - {APP_NAME}</title>
  <meta name="description" content="{APP_NAME} Settings" />
</svelte:head>

<div class="space-y-6">
  <!-- Page Header -->
  <div class="flex justify-between items-center">
    <h1 class="text-3xl font-bold">Settings</h1>
    <div class="flex gap-2">
      <button class="btn btn-ghost" onclick={resetSettings}>Reset</button>
      <button class="btn btn-primary" onclick={saveSettings}>Save Changes</button>
    </div>
  </div>

  <!-- Notification Settings -->
  <div class="card bg-base-100 shadow-lg">
    <div class="card-body">
      <h2 class="card-title">
        <span class="mr-2">🔔</span> Notification Settings
      </h2>
      <div class="space-y-4">
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Email Notifications</span>
            <input
              type="checkbox"
              class="toggle toggle-primary"
              bind:checked={settings.notifications.emailNotifications}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Push Notifications</span>
            <input
              type="checkbox"
              class="toggle toggle-primary"
              bind:checked={settings.notifications.pushNotifications}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Weekly Reports</span>
            <input
              type="checkbox"
              class="toggle toggle-primary"
              bind:checked={settings.notifications.weeklyReports}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Security Alerts</span>
            <input
              type="checkbox"
              class="toggle toggle-primary"
              bind:checked={settings.notifications.securityAlerts}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Marketing Emails</span>
            <input
              type="checkbox"
              class="toggle toggle-primary"
              bind:checked={settings.notifications.marketingEmails}
            />
          </label>
        </div>
      </div>
    </div>
  </div>

  <!-- Privacy Settings -->
  <div class="card bg-base-100 shadow-lg">
    <div class="card-body">
      <h2 class="card-title">
        <span class="mr-2">🔒</span> Privacy Settings
      </h2>
      <div class="space-y-4">
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Share Profile with Team</span>
            <input
              type="checkbox"
              class="toggle toggle-secondary"
              bind:checked={settings.privacy.shareProfile}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Show Online Status</span>
            <input
              type="checkbox"
              class="toggle toggle-secondary"
              bind:checked={settings.privacy.showOnlineStatus}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Allow Direct Messages</span>
            <input
              type="checkbox"
              class="toggle toggle-secondary"
              bind:checked={settings.privacy.allowDirectMessages}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Data Collection for Analytics</span>
            <input
              type="checkbox"
              class="toggle toggle-secondary"
              bind:checked={settings.privacy.dataCollection}
            />
          </label>
        </div>
      </div>
    </div>
  </div>

  <!-- Appearance Settings -->
  <div class="card bg-base-100 shadow-lg">
    <div class="card-body">
      <h2 class="card-title">
        <span class="mr-2">🎨</span> Appearance Settings
      </h2>
      <div class="space-y-4">
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Compact Mode</span>
            <input
              type="checkbox"
              class="toggle toggle-accent"
              bind:checked={settings.appearance.compactMode}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Show Animations</span>
            <input
              type="checkbox"
              class="toggle toggle-accent"
              bind:checked={settings.appearance.showAnimations}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">High Contrast Mode</span>
            <input
              type="checkbox"
              class="toggle toggle-accent"
              bind:checked={settings.appearance.highContrast}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Large Text</span>
            <input
              type="checkbox"
              class="toggle toggle-accent"
              bind:checked={settings.appearance.largeText}
            />
          </label>
        </div>
      </div>
    </div>
  </div>

  <!-- Security Settings -->
  <div class="card bg-base-100 shadow-lg">
    <div class="card-body">
      <h2 class="card-title">
        <span class="mr-2">🛡️</span> Security Settings
      </h2>
      <div class="space-y-4">
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Two-Factor Authentication</span>
            <input
              type="checkbox"
              class="toggle toggle-info"
              bind:checked={settings.security.twoFactorAuth}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Session Timeout</span>
            <input
              type="checkbox"
              class="toggle toggle-info"
              bind:checked={settings.security.sessionTimeout}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Login Alerts</span>
            <input
              type="checkbox"
              class="toggle toggle-info"
              bind:checked={settings.security.loginAlerts}
            />
          </label>
        </div>
        <div class="form-control">
          <label class="label cursor-pointer">
            <span class="label-text">Password Expiry</span>
            <input
              type="checkbox"
              class="toggle toggle-info"
              bind:checked={settings.security.passwordExpiry}
            />
          </label>
        </div>
      </div>
    </div>
  </div>

  <!-- Additional Settings -->
  <div class="card bg-base-100 shadow-lg">
    <div class="card-body">
      <h2 class="card-title">
        <span class="mr-2">⚙️</span> Additional Settings
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="form-control">
          <label class="label">
            <span class="label-text">Language</span>
          </label>
          <select class="select select-bordered">
            <option>English</option>
            <option>Spanish</option>
            <option>French</option>
            <option>German</option>
          </select>
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Timezone</span>
          </label>
          <select class="select select-bordered">
            <option>UTC-08:00 Pacific Time</option>
            <option>UTC-05:00 Eastern Time</option>
            <option>UTC+00:00 GMT</option>
            <option>UTC+01:00 Central European</option>
          </select>
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Date Format</span>
          </label>
          <select class="select select-bordered">
            <option>MM/DD/YYYY</option>
            <option>DD/MM/YYYY</option>
            <option>YYYY-MM-DD</option>
          </select>
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Currency</span>
          </label>
          <select class="select select-bordered">
            <option>USD ($)</option>
            <option>EUR (€)</option>
            <option>GBP (£)</option>
            <option>JPY (¥)</option>
          </select>
        </div>
      </div>
    </div>
  </div>
</div>
