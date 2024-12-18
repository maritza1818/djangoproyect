import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common'; 
import { Discoteca } from '../../models/discoteca.model';

@Component({
  selector: 'app-card-discoteca',
  standalone: true, 
  imports: [CommonModule],
  templateUrl: './card-discoteca.component.html',
  styleUrls: ['./card-discoteca.component.css'],
})
export class CardDiscotecaComponent {
  @Input() discoteca!: Discoteca;
}
