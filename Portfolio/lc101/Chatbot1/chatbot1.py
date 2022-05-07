    def boredGreeting(self, prompt):
        if len(prompt_from_human) >= 20:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else: 
            return Chatbot.response(self, prompt)