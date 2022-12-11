import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { ErrorDialogComponent } from 'src/app/shared/components/error-dialog/error-dialog.component';
import { CoursesService } from '../services/courses.service';

@Component({
  selector: 'app-course-form',
  templateUrl: './course-form.component.html',
  styleUrls: ['./course-form.component.scss']
})
export class CourseFormComponent implements OnInit {

  form: FormGroup

  constructor(
    private formBiulder: FormBuilder,
    private courseService: CoursesService,
    private dialog: MatDialog
  ) {
    this.form = this.formBiulder.group({
      name: [null],
      category: [null]
    })
  }

  onSubmit() {
    let resultado = this.courseService.save(this.form.value);
    if(typeof resultado === 'undefined') this.onError("Erro ao Salvar Cursos! verifique a conexão com a internet ou contate o support.")
    // console.log(typeof(resultado))
    // console.log(this.form.value)
  }

  
  onError(MsgError: String){
    this.dialog.open(ErrorDialogComponent, {
      data: MsgError
    })
    // console.log(MsgError)
  }

  onCancel() { };

  ngOnInit(): void { };

}
