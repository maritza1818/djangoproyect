import { Component, Input } from '@angular/core';
import { Discoteca } from '../../models/discoteca.model';

@Component({
  selector: 'app-card-discoteca',
  templateUrl: './card-discoteca.component.html',
  styleUrls: ['./card-discoteca.component.css'],
})
export class CardDiscotecaComponent {
  @Input() discoteca!: Discoteca;
}
