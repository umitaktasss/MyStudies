class NoteBook:
    def __init__(self, CPU: str, RAM: str, SSD: str, GPU: str, Battery: str, Display: str):
        self.CPU = CPU
        self.RAM = RAM
        self.SSD = SSD
        self.GPU = GPU
        self.Battery = Battery
        self.Display = Display

    def __str__(self) -> str:
        return (f"************\n"
                f"CPU: {self.CPU}\n"
                f"RAM: {self.RAM}\n"
                f"SSD: {self.SSD}\n"
                f"GPU: {self.GPU}\n"
                f"Battery: {self.Battery}\n"
                f"Display: {self.Display}\n"
                f"************\n")

# Example usage:
notebook_A = NoteBook("Intel i7", "16GB DDR4", "512GB", "NVIDIA GTX 1660", "5000mAh", "15.6 inch")
notebook_B = NoteBook("AMD RYZEN 9", "32GB DDR5", "1024GB", "AMD Radeon RX 6800M", "6000mAh", "17.3 inch")
notebook_C = NoteBook("Intel i9", "64GB DDR5", "2056GB", "NVIDIA RTX 4090", "10000mAh", "16 inch")

print(notebook_A)
print(notebook_B)
print(notebook_C)