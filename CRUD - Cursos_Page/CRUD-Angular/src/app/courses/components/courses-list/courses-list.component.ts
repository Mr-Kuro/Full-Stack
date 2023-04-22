import { Component, EventEmitter, Input, Output } from '@angular/core';

import { Course } from '../../interfaces/course';

@Component({
  selector: 'app-courses-list',
  templateUrl: './courses-list.component.html',
  styleUrls: ['./courses-list.component.scss']
})
export class CoursesListComponent {

  @Input() courses: Course[] = [];
  @Output() add = new EventEmitter(false);
  @Output() edit = new EventEmitter(false);
  @Output() delete = new EventEmitter(false)

  readonly displayedColumns = [/*'_id',*/ 'name', 'category', 'duration', 'actions'];

  constructor() { }

  onAdd(){
    console.log('event emitter')
    this.add.emit(true);
  }

  onEdit(course: Course){
    this.edit.emit(course)
  }

  onDelete(course: Course){
    this.delete.emit(course)
  }

}
