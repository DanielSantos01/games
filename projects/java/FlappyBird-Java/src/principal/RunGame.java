package principal;
import java.awt.Graphics;
import java.awt.image.BufferStrategy;

public class RunGame extends Thread{
    private final Settings settings;
    private final Background background;
    private final Ground ground;
    private final Screen screen;
    private final WaitScreen waitScreen;
    private final Bird bird;
    private Graphics paintArea;
    private final Pipe pipe;
    
    public RunGame(Settings config, Background back, Ground base, Screen tela,
            WaitScreen pause, Bird passaro, Pipe cano){
        settings = config;
        background = back;
        ground = base;
        screen = tela;
        waitScreen = pause;
        bird = passaro;
        pipe = cano;
    }
   
    //--------------------------------------------------------------------------------------------------------------------
    @Override
    public void run(){
        while(true){
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
        paintArea = bs.getDrawGraphics();
        updateScreen(screen, background, settings, paintArea, waitScreen, bird, ground, MIN_PRIORITY);
        paintArea.dispose();
        bs.show();
    }
    
    private void updateScreen(Screen screen, Background back, Settings settings, Graphics paintArea, WaitScreen waitScreen, Bird bird,Ground ground, int frames){
        settings.clock(30);
        background.drawBackground(paintArea);
        pipe.draw(paintArea);
        if(settings.preStart || settings.gameOver) pauseScreen(paintArea, settings, bird, ground, waitScreen);
        bird.run(paintArea);
        ground.move(paintArea);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void pauseScreen(Graphics paintArea, Settings settings, Bird bird, Ground ground, WaitScreen waitScreen){
        waitScreen.drawWaitScreen(paintArea);
    }
}
