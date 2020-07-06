package principal;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyEvents implements KeyListener{
    private final Settings settings;
    private Bird bird;
    
    public KeyEvents(Settings config, Bird passarinho){
        settings = config;
        bird = passarinho;
    }

    @Override
    public void keyTyped(KeyEvent ke) {
    }

    @Override
    public void keyPressed(KeyEvent ke) {
        if (ke.getKeyCode() == KeyEvent.VK_SPACE){
            if(settings.preStart || settings.start){
                settings.preStart = false;
                settings.start = true;
                if(bird.bird_rect.y >= 10){
                    settings.fall = settings.birdUpValue;
                }else{
                    settings.fall = 0;
                }
            }else{
                bird.centerBird();
                settings.preStart = true;
                settings.gameOver = false;
            }
        }
    }

    @Override
    public void keyReleased(KeyEvent ke) {
    }
    
}
