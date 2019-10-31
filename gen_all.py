import gan

for i in range(1000):
    print("Generating image ",i)
    gan.gen(i)
    print("Generated image ",i)
