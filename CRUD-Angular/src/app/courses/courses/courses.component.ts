import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { catchError, Observable, of } from 'rxjs';
import { ErrorDialogComponent } from 'src/app/shared/components/error-dialog/error-dialog.component';
import { Course } from '../models/course';
import { CoursesService } from '../services/courses.service';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.scss']
})
export class CoursesComponent implements OnInit {

  // observables de curses[] e apenas Curse[]
  // public coursees: Course[] = [];    // teste* apenas Curse[]
  public courses$: Observable<Course[]>;    // observable de Curse[]

  // array de colunas para mostrar no mat...
  displayedColumns = ['name', 'category', 'duration'];


  // coursesService: CoursesService;  // outra forma de inicializar fora do construtor da classe

  constructor(
    private coursesService: CoursesService,
    public dialog: MatDialog
    ) {
    // this.coursesService;   // forma de inicializar fora do parâmetro do construtor da classe
    // this.coursesService = new CoursesService();   // inicializando fora do parâmetro do construtor

    this.courses$ = this.coursesService.list().pipe(
      catchError(error => {
        // console.log(error)
        this.onError("Erro ao carregar Cursos Disponíveis!\n Contate o Support!")
        return of([]);
      })
    );
    /* testes* com coursees: Course[]
      this.courses.subscribe(course => this.coursees = course as [])
      console.log('>>>>>>>>>>>>>>>>>>>>>>>>>'); 
      console.log(this.coursees);
      console.log("<<<<<<<<<<<<<<<<<<<<<<<<<")
    */
  }

  onError(ErrorMsg: string) {
    this.dialog.open(ErrorDialogComponent, {
      data:
        ErrorMsg
    })
  }

  ngOnInit(): void {
    /* testes com courses: Observable<Course[]> e coursees: Course[]
      this.courses.subscribe(courses => this.coursees = courses)
      console.log('this.coursees');
      console.log(this.coursees);
      console.log('this.coursees');
    */
  }

}
