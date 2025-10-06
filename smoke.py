import botbook_mcp3002 as mcp

smokeLevel= 0

def isFire() -> bool:
    global smokeLevel
    smokeLevel= mcp.readAnalog()
    print(smokeLevel)
    if smokeLevel > 120:
        return True

def main():
    isFire()

if __name__=="__main__":
    main()