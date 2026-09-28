aantalAppels = int(input())
aantalKisten = aantalAppels // 20
aantalAppels = aantalAppels % 20
aantalPaletten = aantalKisten // 35
aantalKisten = aantalKisten % 35
print(aantalPaletten)
print(aantalKisten)
print(aantalAppels)