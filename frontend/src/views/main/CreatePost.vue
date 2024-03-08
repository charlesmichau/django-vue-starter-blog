<template>
  <div class="flex flex-col my-4 py-4 space-y-10 border-t-2">

    <!-- If the user is not authenticated -->
    <div v-if="!this.user.isAuthenticated">
      You need to
      <router-link
        to="/account"
        class="text-teal-500 hover:underline hover:text-teal-700"
        >sign in</router-link
      >
      before you can leave your comment.
    </div>

    <!-- If the user is authenticated -->
    <div v-else>

      <!-- If post is submitted -->
      <div v-if="this.postSubmitSuccess" class="">
        <p class="font-bold text-2xl">Thank you ! 🎉</p>
        Your comment will show up here after is has been approved.
      </div>

      <!-- If post is being created -->
      <div v-else class="">
        <p class="font-bold text-2xl">Write your post below:</p>
        <p>Object: {{this.title}} - {{this.selectedObject}}</p>

        <form action="POST" @submit.prevent="createPost" @mouseup="handleSelection">
          <textarea
            type="text"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
            rows="1"
            v-model="title"
            placeholder= "Title"
          />

          <textarea
            type="text"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
            rows="5"
            v-model="content"
            placeholder="Content"
          />

          <button
            class="mt-4 w-full bg-teal-500 hover:bg-teal-700 focus:ring focus:ring-teal-100 text-white py-2 rounded-md text-lg tracking-wide"
          >

          Submit Post
        </button>
      </form>

      <form v-if="this.selectedObject" @submit.prevent="submitForm">
        <label for="property1">Property 1:</label>
        <input v-model="this.selectedObject.property1" id="property1" />

        <label for="property2">Property 2:</label>
        <input v-model="this.selectedObject.property2" id="property2" />

        <button type="submit">Submit</button>
      </form>

      </div>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/user";
import { SUBMIT_POST } from "@/mutations";

export default {
  name: "CreatePostView",

  setup() {
    const userStore = useUserStore();
    return { userStore };
  },

  data() {
    return {
      title: null,
      content: null,
      user: {
        isAuthenticated: false,
        token: this.userStore.getToken || "",
        info: this.userStore.getUser || {},
      },
      userID: null,
      postSubmitSuccess: false,
      selectedObject: null,
    };
  },

  async created() {
    if (this.user.token) {
      this.user.isAuthenticated = true;
      this.user;
    }
    this.userID = JSON.parse(localStorage.getItem("user")).id;
  },

  methods: {
    createPost() {
      console.log("Logging ", this.title, this.content, this.user.info.id);
      this.$apollo
        .mutate({
          mutation: SUBMIT_POST,
          variables: {
            title: this.title,
            content: this.content,
            userID: this.user.info.id,
          },
        })
        .then(() => (this.postSubmitSuccess = true))
        .catch((error) => {
          this.error = error;
          alert("E " + error);
        });
    },
    handleSelection() {
      console.log("Logging call to handleSelection");
      const selectedText = window.getSelection().toString();
      if (selectedText) {
        this.selectedObject = { text: selectedText, property1: "", property2: "" };
      } else {
        this.selectedObject = null;
      }
    },
  },
};
</script>
