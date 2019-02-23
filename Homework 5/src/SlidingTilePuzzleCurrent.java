import csis4463.SlidingTilePuzzle;
import java.util.ArrayList;
/*
 * @author Brain Fox and Greg Walsh
 * ______      _              ______                          _   _____                  _    _       _     _     
 *  ___ \    (_)             |  ___|                        | | |  __ \                | |  | |     | |   | |    
 *| |_/ /_ __ _  __ _ _ __   | |_ _____  __   __ _ _ __   __| | | |  \/_ __ ___  __ _  | |  | | __ _| |___| |__  
 *| ___ \ '__| |/ _` | '_ \  |  _/ _ \ \/ /  / _` | '_ \ / _` | | | __| '__/ _ \/ _` | | |/\| |/ _` | / __| '_ \ 
 *| |_/ / |  | | (_| | | | | | || (_) >  <  | (_| | | | | (_| | | |_\ \ | |  __/ (_| | \  /\  / (_| | \__ \ | | |
 *\____/|_|  |_|\__,_|_| |_| \_| \___/_/\_\  \__,_|_| |_|\__,_|  \____/_|  \___|\__, |  \/  \/ \__,_|_|___/_| |_|
 *                                                                               __/ |                           
 *                                                                             |___/                            
 *
 */

/*
 * Wrapper class for SlidingTilePuzzle 
 */
public class SlidingTilePuzzleCurrent{
	private SlidingTilePuzzle stp;
	private ArrayList<SlidingTilePuzzle> path;
	
	/*
	 * Initialize wrapper with pathe only containing current puzzle
	 */
	public SlidingTilePuzzleCurrent(SlidingTilePuzzle stp){
		this.stp = stp;
		this.path = new ArrayList<SlidingTilePuzzle>();
		this.path.add(stp);
	}	
	
	/*
	 * Used by successor function to initialize puzzles with a path
	 */
	private SlidingTilePuzzleCurrent(SlidingTilePuzzle stp, ArrayList<SlidingTilePuzzle> path){
		this.stp = stp;
		this.path = new ArrayList<>(path);
		this.path.add(stp);

	}

	public ArrayList<SlidingTilePuzzle> getPath(){
		return path;
	}

	/*
	 * calculate priority using path length and sum of manhattan distances
	 */
	public int getPriority(){
		int manhattanDistance=0;
		//for each row
		for(int i=0;i<stp.numRows();i++){
			//for each column
			for(int j=0;j<stp.numColumns();j++){
				//value in current tile
				int tile = stp.getTile(i,j);
				//calculate which tile that value belongs to
				int adjusted = tile==0 ? 8 : tile-1;
				int goalRow = adjusted/stp.numColumns();
				int goalColumn = adjusted%stp.numColumns();
				//calculate and sum  manhattan distance
				manhattanDistance += Math.abs(i-goalRow) + Math.abs(j-goalColumn);
				

			}

		}
		//less one to account for the current state being in path
		return manhattanDistance+path.size();
		
	}
	
	/*
	 *  return unique string representation of board state the make a hashable value to use to look up board states
	 */
	public String getHashValue(){

		StringBuilder sb = new StringBuilder();
		for(int i=0;i<stp.numRows();i++){
			
			for(int j=0;j<stp.numColumns();j++){
				//append each tile to a string in order
				sb.append(stp.getTile(i,j));

			}

		}

		return sb.toString();

	}

	public boolean isGoalState(){
		return stp.isGoalState();
	}

	public ArrayList<SlidingTilePuzzleCurrent> getSuccessors(){
		
		ArrayList<SlidingTilePuzzleCurrent> successors = new ArrayList<>(4);
		
		//box each successor into a wrapper 
		for(SlidingTilePuzzle puzzle : stp.getSuccessors()){
			successors.add(new SlidingTilePuzzleCurrent(puzzle,path));
		}

		return successors;
	}

	public String toString(){
		return stp.toString();
	}
}
