import { Component, Input, OnInit } from '@angular/core';
import { GameStates, Players, TicTacToeService } from '../tic-tac-toe.service';
import { SafeHtml } from '@angular/platform-browser';

@Component({
  selector: 'app-tic-tac-toe-square',
  templateUrl: './tic-tac-toe-square.component.html',
  styleUrls: ['./tic-tac-toe-square.component.css']
})
export class TicTacToeSquareComponent implements OnInit {

  @Input() square: any;
  xHtml: SafeHtml = '<i id="cross" class="fas fa-times"></i>';
  oHtml: SafeHtml = '<i id="circle" class="far fa-circle"></i>';

  constructor(public gameService: TicTacToeService) {
  }

  ngOnInit(): void {
  }

  drawCircleCross(): SafeHtml {
    return (this.square.state === Players.PlayerX) ? this.xHtml : this.oHtml;
  }

  makeMove(): void {
    if (this.gameService.gameState == GameStates.Running && this.square.state === null) {
      this.square.state = this.gameService.gameTurn;
      this.gameService.makeMove(this.square);
    }
  }

}
