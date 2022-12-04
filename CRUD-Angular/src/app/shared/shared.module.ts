import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { AppMaterialModule } from './app-material/app-material.module';
import { ErrorDialogComponent } from './components/error-dialog/error-dialog.component';
import { CategoryPipe } from './pipes/category.pipe';
import { DurationPipe } from './pipes/duration.pipe';
import { IdPipe } from './pipes/-id.pipe';
import { NamePipe } from './pipes/name.pipe';



@NgModule({
  declarations: [
    ErrorDialogComponent,
    CategoryPipe,
    DurationPipe,
    IdPipe,
    NamePipe
  ],
  imports: [
    CommonModule,
    AppMaterialModule
  ],
  exports: [
    ErrorDialogComponent,
    CategoryPipe,
    IdPipe,
    DurationPipe,
    NamePipe
  ],
})
export class SharedModule { }
