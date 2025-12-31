<script>
  import { APP_NAME } from "$lib/config.js";

  // Mock data for demo
  const stats = {
    totalUsers: 24,
    activeUsers: 18,
    newUsers: 6,
    departments: 4,
  };
</script>

<svelte:head>
  <title>Dashboard - {APP_NAME}</title>
  <meta name="description" content="{APP_NAME} Dashboard" />
</svelte:head>

<div class="space-y-6">
  <!-- Page Header -->
  <div class="flex justify-between items-center">
    <h1 class="text-3xl font-bold">Dashboard</h1>
    <div class="flex gap-2">
      <button class="btn btn-primary">Add User</button>
      <button class="btn btn-outline">Export</button>
    </div>
  </div>

  <!-- Stats Cards -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
    <div class="stat bg-base-100 shadow-lg rounded-lg">
      <div class="stat-figure text-primary">
        <span class="text-4xl">👥</span>
      </div>
      <div class="stat-title">Total Users</div>
      <div class="stat-value text-primary">{stats.totalUsers}</div>
      <div class="stat-desc">All employees</div>
    </div>

    <div class="stat bg-base-100 shadow-lg rounded-lg">
      <div class="stat-figure text-secondary">
        <span class="text-4xl">✅</span>
      </div>
      <div class="stat-title">Active Users</div>
      <div class="stat-value text-secondary">{stats.activeUsers}</div>
      <div class="stat-desc">Currently active</div>
    </div>

    <div class="stat bg-base-100 shadow-lg rounded-lg">
      <div class="stat-figure text-accent">
        <span class="text-4xl">🆕</span>
      </div>
      <div class="stat-title">New Users</div>
      <div class="stat-value text-accent">{stats.newUsers}</div>
      <div class="stat-desc">This month</div>
    </div>

    <div class="stat bg-base-100 shadow-lg rounded-lg">
      <div class="stat-figure text-info">
        <span class="text-4xl">🏢</span>
      </div>
      <div class="stat-title">Departments</div>
      <div class="stat-value text-info">{stats.departments}</div>
      <div class="stat-desc">Total departments</div>
    </div>
  </div>

  <!-- Quick Actions -->
  <div class="card bg-base-100 shadow-lg">
    <div class="card-body">
      <h2 class="card-title">Quick Actions</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <a href="/users" class="btn btn-outline btn-block">
          <span class="mr-2">👥</span> Manage Users
        </a>
        <a href="/settings" class="btn btn-outline btn-block">
          <span class="mr-2">⚙️</span> Settings
        </a>
        <button class="btn btn-outline btn-block">
          <span class="mr-2">📊</span> Reports
        </button>
      </div>
    </div>
  </div>

  <!-- Recent Activity -->
  <div class="card bg-base-100 shadow-lg">
    <div class="card-body">
      <h2 class="card-title">Recent Activity</h2>
      <div class="space-y-3">
        <div class="flex items-center justify-between p-3 bg-base-200 rounded">
          <div class="flex items-center gap-3">
            <span class="text-2xl">👤</span>
            <div>
              <p class="font-medium">John Doe added</p>
              <p class="text-sm opacity-70">2 hours ago</p>
            </div>
          </div>
          <span class="badge badge-success">New</span>
        </div>
        <div class="flex items-center justify-between p-3 bg-base-200 rounded">
          <div class="flex items-center gap-3">
            <span class="text-2xl">✏️</span>
            <div>
              <p class="font-medium">Jane Smith updated</p>
              <p class="text-sm opacity-70">5 hours ago</p>
            </div>
          </div>
          <span class="badge badge-info">Updated</span>
        </div>
        <div class="flex items-center justify-between p-3 bg-base-200 rounded">
          <div class="flex items-center gap-3">
            <span class="text-2xl">🗑️</span>
            <div>
              <p class="font-medium">Bob Wilson removed</p>
              <p class="text-sm opacity-70">1 day ago</p>
            </div>
          </div>
          <span class="badge badge-error">Removed</span>
        </div>
      </div>
    </div>
  </div>
</div>
