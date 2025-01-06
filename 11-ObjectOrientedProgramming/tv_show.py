from tv import TV

def main():
    tv1 = TV()
    tv1.show_status()
    tv1.turn_on()
    tv1.show_status()
    tv1.turn_off()
    tv1.show_status()
    tv1.show_channels()
    tv1.set_channels("TVP1 TVP2 Polsat TVN Filmbox Discovery")
    tv1.show_channels()
    tv1.turn_on()
    tv1.set_channel(4)
    tv1.show_status()
    

if __name__ == "__main__":
    main()