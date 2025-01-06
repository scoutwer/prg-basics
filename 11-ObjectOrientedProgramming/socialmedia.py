class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
    def display_timeline(self):
        n = 1 
        print("Timeline: ")
        for i in self.posts:
            print(str(n) + ". " + i)
            n = n + 1

def main():
    johndoe = SocialMediaProfile(username="johndoe")
    johndoe.add_post(content= "Hello, world!")
    johndoe.add_post(content= "Had a great day at the park!")
    johndoe.add_post(content= "What's up, Natalie? How are you?")
    johndoe.display_timeline()


if __name__ == "__main__":
    main()
