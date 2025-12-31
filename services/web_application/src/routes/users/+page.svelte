<script>
  import { APP_NAME } from "$lib/config.js";

  // Mock user data
  let users = $state([
    {
      id: 1,
      name: "John Doe",
      email: "john@company.com",
      department: "Engineering",
      role: "Developer",
      status: "active",
    },
    {
      id: 2,
      name: "Jane Smith",
      email: "jane@company.com",
      department: "HR",
      role: "Manager",
      status: "active",
    },
    {
      id: 3,
      name: "Bob Wilson",
      email: "bob@company.com",
      department: "Sales",
      role: "Sales Rep",
      status: "inactive",
    },
    {
      id: 4,
      name: "Alice Brown",
      email: "alice@company.com",
      department: "Engineering",
      role: "Designer",
      status: "active",
    },
    {
      id: 5,
      name: "Charlie Davis",
      email: "charlie@company.com",
      department: "Marketing",
      role: "Marketing Lead",
      status: "active",
    },
  ]);

  // Form state
  let showAddModal = $state(false);
  let showEditModal = $state(false);
  let editingUser = $state(null);
  let formData = $state({
    name: "",
    email: "",
    department: "",
    role: "",
    status: "active",
  });

  // Search and filter
  let searchTerm = $state("");
  let filterDepartment = $state("all");

  const departments = ["Engineering", "HR", "Sales", "Marketing"];
  const roles = ["Developer", "Manager", "Sales Rep", "Designer", "Marketing Lead"];

  // Computed filtered users
  const filteredUsers = $derived(
    users.filter((user) => {
      const matchesSearch =
        user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        user.email.toLowerCase().includes(searchTerm.toLowerCase());
      const matchesDepartment = filterDepartment === "all" || user.department === filterDepartment;
      return matchesSearch && matchesDepartment;
    }),
  );

  function openAddModal() {
    formData = { name: "", email: "", department: "", role: "", status: "active" };
    showAddModal = true;
  }

  function openEditModal(user) {
    editingUser = user;
    formData = { ...user };
    showEditModal = true;
  }

  function addUser() {
    const newUser = {
      id: Math.max(...users.map((u) => u.id)) + 1,
      ...formData,
    };
    users = [...users, newUser];
    showAddModal = false;
  }

  function updateUser() {
    users = users.map((user) => (user.id === editingUser.id ? { ...user, ...formData } : user));
    showEditModal = false;
    editingUser = null;
  }

  function deleteUser(userId) {
    users = users.filter((user) => user.id !== userId);
  }

  function cancelModal() {
    showAddModal = false;
    showEditModal = false;
    editingUser = null;
  }
</script>

<svelte:head>
  <title>Users - {APP_NAME}</title>
  <meta name="description" content="{APP_NAME} User Management" />
</svelte:head>

<div class="space-y-6">
  <!-- Page Header -->
  <div class="flex justify-between items-center">
    <h1 class="text-3xl font-bold">User Management</h1>
    <button class="btn btn-primary" onclick={openAddModal}>
      <span class="mr-2">➕</span> Add User
    </button>
  </div>

  <!-- Filters -->
  <div class="card bg-base-100 shadow-lg">
    <div class="card-body">
      <div class="flex flex-col md:flex-row gap-4">
        <div class="flex-1">
          <input
            type="text"
            placeholder="Search users..."
            class="input input-bordered w-full"
            bind:value={searchTerm}
          />
        </div>
        <div class="form-control">
          <select class="select select-bordered" bind:value={filterDepartment}>
            <option value="all">All Departments</option>
            {#each departments as dept}
              <option value={dept}>{dept}</option>
            {/each}
          </select>
        </div>
      </div>
    </div>
  </div>

  <!-- Users Table -->
  <div class="card bg-base-100 shadow-lg">
    <div class="card-body p-0">
      <div class="overflow-x-auto">
        <table class="table table-zebra w-full">
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Department</th>
              <th>Role</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {#each filteredUsers as user}
              <tr>
                <td>
                  <div class="flex items-center gap-3">
                    <div class="avatar placeholder">
                      <div class="bg-neutral text-neutral-content rounded-full w-12">
                        <span class="text-lg"
                          >{user.name
                            .split(" ")
                            .map((n) => n[0])
                            .join("")}</span
                        >
                      </div>
                    </div>
                    <span class="font-medium">{user.name}</span>
                  </div>
                </td>
                <td>{user.email}</td>
                <td>{user.department}</td>
                <td>{user.role}</td>
                <td>
                  <span class="badge {user.status === 'active' ? 'badge-success' : 'badge-error'}">
                    {user.status}
                  </span>
                </td>
                <td>
                  <div class="flex gap-2">
                    <button class="btn btn-ghost btn-sm" onclick={() => openEditModal(user)}>
                      ✏️
                    </button>
                    <button
                      class="btn btn-ghost btn-sm btn-error"
                      onclick={() => deleteUser(user.id)}
                    >
                      🗑️
                    </button>
                  </div>
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>

<!-- Add User Modal -->
{#if showAddModal}
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Add New User</h3>
      <div class="py-4 space-y-4">
        <div class="form-control">
          <label class="label">
            <span class="label-text">Name</span>
          </label>
          <input type="text" class="input input-bordered" bind:value={formData.name} />
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Email</span>
          </label>
          <input type="email" class="input input-bordered" bind:value={formData.email} />
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Department</span>
          </label>
          <select class="select select-bordered" bind:value={formData.department}>
            <option value="">Select Department</option>
            {#each departments as dept}
              <option value={dept}>{dept}</option>
            {/each}
          </select>
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Role</span>
          </label>
          <select class="select select-bordered" bind:value={formData.role}>
            <option value="">Select Role</option>
            {#each roles as role}
              <option value={role}>{role}</option>
            {/each}
          </select>
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Status</span>
          </label>
          <select class="select select-bordered" bind:value={formData.status}>
            <option value="active">Active</option>
            <option value="inactive">Inactive</option>
          </select>
        </div>
      </div>
      <div class="modal-action">
        <button class="btn btn-ghost" onclick={cancelModal}>Cancel</button>
        <button class="btn btn-primary" onclick={addUser}>Add User</button>
      </div>
    </div>
  </div>
{/if}

<!-- Edit User Modal -->
{#if showEditModal}
  <div class="modal modal-open">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Edit User</h3>
      <div class="py-4 space-y-4">
        <div class="form-control">
          <label class="label">
            <span class="label-text">Name</span>
          </label>
          <input type="text" class="input input-bordered" bind:value={formData.name} />
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Email</span>
          </label>
          <input type="email" class="input input-bordered" bind:value={formData.email} />
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Department</span>
          </label>
          <select class="select select-bordered" bind:value={formData.department}>
            <option value="">Select Department</option>
            {#each departments as dept}
              <option value={dept}>{dept}</option>
            {/each}
          </select>
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Role</span>
          </label>
          <select class="select select-bordered" bind:value={formData.role}>
            <option value="">Select Role</option>
            {#each roles as role}
              <option value={role}>{role}</option>
            {/each}
          </select>
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Status</span>
          </label>
          <select class="select select-bordered" bind:value={formData.status}>
            <option value="active">Active</option>
            <option value="inactive">Inactive</option>
          </select>
        </div>
      </div>
      <div class="modal-action">
        <button class="btn btn-ghost" onclick={cancelModal}>Cancel</button>
        <button class="btn btn-primary" onclick={updateUser}>Update User</button>
      </div>
    </div>
  </div>
{/if}
