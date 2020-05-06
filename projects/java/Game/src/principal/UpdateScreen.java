package principal;
import java.awt.Graphics;


public class UpdateScreen {
    
    public UpdateScreen(){
            
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void update(Screen screen, Background back, Settings settings, Graphics paintArea, WaitScreen waitScreen, Bird bird,Ground ground, int frames){
        settings.clock(35);
        back.drawBackground(paintArea);
        if(settings.preStart || settings.gameOver) pauseScreen(paintArea, settings, bird, ground, waitScreen);
        bird.run(paintArea);
        ground.update(paintArea);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void pauseScreen(Graphics paintArea, Settings settings, Bird bird, Ground ground, WaitScreen waitScreen){
        waitScreen.drawWaitScreen(paintArea);
    }
}
