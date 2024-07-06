def appExec():       
    app.exec_()
    Global.done = True
    timer = time.time()
    while time.time() - timer < 0.8:
        print("waiting process to close")        