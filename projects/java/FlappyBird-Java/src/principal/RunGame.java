package principal;
import java.awt.Graphics;
import java.awt.image.BufferStrategy;

public class RunGame extends Thread{
    private final Settings settings;
    private final Background background;
    private final Ground ground;
    private final Screen screen;
    private final UpdateScreen updateScreen;
    private final WaitScreen waitScreen;
    private final Bird bird;
    private Graphics paintAarea;
    
    public RunGame(Settings config, Background back, Ground base, Screen tela, UpdateScreen up, WaitScreen pause, Bird passaro){
        settings = config;
        background = back;
        ground = base;
        screen = tela;
        updateScreen = up;
        waitScreen = pause;
        bird = passaro;
    }
   
    //--------------------------------------------------------------------------------------------------------------------
    @Override
    public void run(){
        while(true){
            settings.wait(15f);
            render();
        }
        
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void render(){
        BufferStrategy bs = settings.canvas.getBufferStrategy();
        if(bs == null) {
            settings.canvas.createBufferStrategy(2);
            return;
        }
        paintAarea = bs.getDrawGraphics();
        updateScreen.update(screen, background, settings, paintAarea, waitScreen, bird, ground, MIN_PRIORITY);
        paintAarea.dispose();
        bs.show();
    }
}
