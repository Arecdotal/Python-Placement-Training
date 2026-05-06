class A:
    def start(self):
        print("A Started...")
        
class B(A):
    def start(self):
        super().start()
        print("B Started...")
            
if __name__ == "__main__":
    b = B()
    b.start()