<script>
  import "./layout.css";
  import { page } from "$app/stores";
  import { APP_NAME } from "$lib/config.js";

  /** @type {{children: import('svelte').Snippet}} */
  let { children } = $props();

  const navItems = [
    { href: "/", label: "Dashboard", icon: "📊" },
    { href: "/users", label: "Users", icon: "👥" },
    { href: "/settings", label: "Settings", icon: "⚙️" },
  ];
</script>

<div class="drawer drawer-mobile">
  <input id="drawer-toggle" type="checkbox" class="drawer-toggle" />

  <!-- Main Content -->
  <div class="drawer-content flex flex-col">
    <!-- Header -->
    <header class="navbar bg-base-100 shadow-lg">
      <div class="flex-none lg:hidden">
        <label for="drawer-toggle" class="btn btn-square btn-ghost">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            ></path>
          </svg>
        </label>
      </div>
      <div class="flex-1">
        <h1 class="text-xl font-bold">{APP_NAME}</h1>
      </div>
      <div class="flex-none">
        <div class="dropdown dropdown-end">
          <label tabindex="0" class="btn btn-ghost btn-circle avatar">
            <div
              class="w-10 rounded-full bg-primary text-primary-content flex items-center justify-center"
            >
              <span class="text-lg">👤</span>
            </div>
          </label>
          <ul
            tabindex="0"
            class="mt-3 p-2 shadow menu menu-compact dropdown-content bg-base-100 rounded-box w-52"
          >
            <li><a>Profile</a></li>
            <li><a>Logout</a></li>
          </ul>
        </div>
      </div>
    </header>

    <!-- Page Content -->
    <main class="flex-1 p-6 overflow-auto">
      {@render children()}
    </main>
  </div>

  <!-- Sidebar -->
  <div class="drawer-side">
    <label for="drawer-toggle" class="drawer-overlay"></label>
    <aside class="w-64 min-h-full bg-base-200">
      <div class="p-4">
        <h2 class="text-lg font-bold mb-6">Navigation</h2>
        <ul class="menu menu-vertical p-0 space-y-2">
          {#each navItems as item}
            <li>
              <a
                href={item.href}
                class="flex items-center gap-3 {$page.url.pathname === item.href ? 'active' : ''}"
              >
                <span class="text-xl">{item.icon}</span>
                <span>{item.label}</span>
              </a>
            </li>
          {/each}
        </ul>
      </div>
    </aside>
  </div>
</div>
