class Solution {
public:
    bool isRobotBounded(string instructions) {
        int posX = 0;
        int posY = 0;
        char orientation = 'N';
        for (int i=0; i<instructions.length(); ++i){
            if (instructions[i] == 'G'){
                switch (orientation) {
                    case 'N':
                        posY++;
                        break;
                    case 'S':
                        posY--;
                        break;
                    case 'E':
                        posX++;
                        break;
                    case 'W':
                        posX--;
                        break;
                }
            }else if (instructions[i] == 'L'){
                switch (orientation) {
                    case 'N':
                        orientation = 'W';
                        break;
                    case 'S':
                        orientation = 'E';
                        break;
                    case 'E':
                        orientation = 'N';
                        break;
                    case 'W':
                        orientation = 'S';
                        break;
                }
            }else if (instructions[i] == 'R'){
                switch (orientation) {
                    case 'N':
                        orientation = 'E';
                        break;
                    case 'S':
                        orientation = 'W';
                        break;
                    case 'E':
                        orientation = 'S';
                        break;
                    case 'W':
                        orientation = 'N';
                        break;
                }
            }
        }
        if ((posX == 0 && posY == 0) || orientation != 'N')
            return true;
        return false;
    }
};